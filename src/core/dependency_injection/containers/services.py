from dependency_injector import containers, providers

from services.health import HealthCheckService


class ServicesContainer(containers.DeclarativeContainer):
    settings = providers.DependenciesContainer()

    health_service: providers.Factory[HealthCheckService] = providers.Factory(
        HealthCheckService, project_settings=settings.project_settings
    )
