from redis.asyncio.client import Pipeline
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session

from core.clients.redis_client import RedisClient
from core.persistance.connection_managers.postgres import PostgresConnectionManager
from core.persistance.unit_of_work import UnitOfWork
from health.domain.health import Health
from health.persistence.orm.health import HealthModel


class HealthRepository:
    def __init__(
        self,
        uow: UnitOfWork,
        postgres_connection_manager: PostgresConnectionManager,
        redis_client: RedisClient,
    ):
        self.uow = uow
        self.postgres_read_session_factory = (
            postgres_connection_manager.get_read_session_factory()
        )
        self.redis_client = redis_client
        self.CACHE_EXPIRATION = 60 * 60 * 24  # 24 hours

    async def save(self, health: Health) -> Health:
        """
        Save the health status to the database and cache.

        Args:
            health (Health): The health status to save.

        Returns:
            Health: The saved health status.
        """

        async def postgres_operation(session: Session, health: Health) -> HealthModel:
            health_model = HealthModel(
                app_name=health.app_name, status=health.status, message=health.message
            )
            session.add(health_model)
            return health_model

        async def redis_operation(redis_client, health: Health):
            key = f"health:{health.app_name}"
            value = health.model_dump_json()
            redis_client.set(key, value, ex=self.CACHE_EXPIRATION)

        await self.uow.execute_postgres(operation=postgres_operation, health=health)
        await self.uow.execute_redis(operation=redis_operation, health=health)

        return health

    async def update(self, health: Health) -> Health:
        """
        Update the health status in the database and cache.

        Args:
            health (Health): The health status to update.

        Returns:
            Health: The updated health status.
        """

        async def postgres_operation(
            session: AsyncSession, health: Health
        ) -> HealthModel:
            health_stored = await session.execute(
                select(HealthModel).filter_by(app_name=health.app_name)
            )
            health_model: HealthModel | None = health_stored.scalars().first()
            if health_model:
                health_model.status = health.status
                health_model.message = health.message
                session.add(health_model)
                return health_model
            else:
                raise ValueError("Health record not found for update.")

        async def redis_operation(redis_client: Pipeline, health: Health):
            key = f"health:{health.app_name}"
            value = health.model_dump_json()
            redis_client.set(key, value, ex=self.CACHE_EXPIRATION)

        await self.uow.execute_postgres(operation=postgres_operation, health=health)
        await self.uow.execute_redis(operation=redis_operation, health=health)

        return health

    async def get(self, app_name: str) -> Health | None:
        """
        Get the health status from the cache or database.

        Args:
            app_name (str): The name of the application.

        Returns:
            Health | None: The health status if found, otherwise None.
        """
        key = f"health:{app_name}"
        cached_health = await self.redis_client.get(key)
        if cached_health:
            return Health.model_validate_json(cached_health, strict=True)

        session = self.postgres_read_session_factory()
        try:
            result = await session.execute(
                select(HealthModel).filter_by(app_name=app_name)
            )
            health_model = result.scalars().first()
            if health_model:
                return Health.model_validate(health_model, strict=True)
            return None
        finally:
            await session.close()
