from dependency_injector import containers, providers

from health.services.health import HealthCheckService


class ServicesContainer(containers.DeclarativeContainer):
    core_settings = providers.DependenciesContainer()
    persistance = providers.DependenciesContainer()

    health_service = providers.Factory(
        HealthCheckService,
        project_settings=core_settings.project_settings,
        health_repository=persistance.health_repository,
    )
