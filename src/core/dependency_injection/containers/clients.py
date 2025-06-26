from dependency_injector import containers, providers

from core.clients.redis_client import RedisClient


class CoreClientsContainer(containers.DeclarativeContainer):
    core_settings = providers.DependenciesContainer()
    core_persistance = providers.DependenciesContainer()

    redis_client = providers.Singleton(
        RedisClient, redis_connection_manager=core_persistance.redis_connection_manager
    )
