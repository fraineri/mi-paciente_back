from dependency_injector import containers, providers

from use_cases.health.check_get_health import CheckGetHealth


class UseCasesContainer(containers.DeclarativeContainer):
    services = providers.DependenciesContainer()

    health_check_get: providers.Factory[CheckGetHealth] = providers.Factory(
        CheckGetHealth, health_check_service=services.health_service
    )
