from dependency_injector import containers, providers

from health.persistence.repositories.health_repository import HealthRepository


class PersistanceContainer(containers.DeclarativeContainer):
    core_persistance = providers.DependenciesContainer()
    core_clients = providers.DependenciesContainer()

    health_repository = providers.Singleton(
        HealthRepository,
        uow=core_persistance.uow,
        postgres_connection_manager=core_persistance.postgres_connection_manager,
        redis_client=core_persistance.redis_client,
    )
