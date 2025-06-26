from typing import Callable, Coroutine, TypeVar

from redis.asyncio.client import Pipeline, Redis
from sqlalchemy.ext.asyncio import AsyncSession

from core.persistance.connection_managers.postgres import PostgresConnectionManager
from core.persistance.connection_managers.redis import RedisConnectionManager

T = TypeVar("T")


class UnitOfWork:
    """
    An asynchronous implementation of the Unit of Work pattern for managing
    transactions across PostgreSQL and Redis.
    """

    def __init__(
        self,
        postgres_connection_manager: PostgresConnectionManager,
        redis_connection_manager: RedisConnectionManager,
    ):
        self._postgres_connection_manager = postgres_connection_manager
        self._redis_connection_manager = redis_connection_manager

    async def __aenter__(self):
        postgres_session_factory = (
            self._postgres_connection_manager.get_write_session_factory()
        )
        self.postgres_session: AsyncSession = postgres_session_factory()

        redis_conn: Redis = self._redis_connection_manager.get_connection()
        self.redis_pipeline: Pipeline = redis_conn.pipeline()

        return self

    async def __aexit__(self, *args):
        await self.postgres_session.close()
        await self.redis_pipeline.connection_pool.disconnect()

    async def commit(self):
        await self.postgres_session.commit()
        await self.redis_pipeline.execute()

    async def rollback(self):
        await self.postgres_session.rollback()
        await self.redis_pipeline.reset()

    async def execute_postgres(
        self, operation: Callable[..., Coroutine[None, None, T]], *args, **kwargs
    ) -> T:
        """
        Executes a PostgreSQL operation within the current transaction.
        """
        return await operation(self.postgres_session, *args, **kwargs)

    async def execute_redis(
        self, operation: Callable[..., Coroutine[None, None, T]], *args, **kwargs
    ) -> T:
        """
        Executes a Redis operation within the current transaction pipeline.
        """
        return await operation(self.redis_pipeline, *args, **kwargs)
