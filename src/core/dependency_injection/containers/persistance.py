from typing import cast

from dependency_injector import containers, providers

from core.dependency_injection.containers.settings import CoreSettingsContainer
from core.persistance.connection_managers.postgres import PostgresConnectionManager
from core.persistance.connection_managers.redis import RedisConnectionManager
from core.persistance.unit_of_work import UnitOfWork


class CorePersistanceContainer(containers.DeclarativeContainer):
    settings = cast(CoreSettingsContainer, providers.DependenciesContainer())

    # Connection Managers
    postgres_connection_manager = providers.Singleton(
        PostgresConnectionManager, settings=settings.postgres_settings
    )
    redis_connection_manager = providers.Singleton(
        RedisConnectionManager, settings=settings.redis_settings
    )

    # Unit of Work
    unit_of_work = providers.Singleton(
        UnitOfWork,
        postgres_connection_manager=postgres_connection_manager,
        redis_connection_manager=redis_connection_manager,
    )
