from typing import cast

from dependency_injector import containers, providers

from health.dependency_injection.containers.services import ServicesContainer
from health.use_cases.check_health import CheckHealth


class UseCasesContainer(containers.DeclarativeContainer):
    services: ServicesContainer = cast(
        ServicesContainer, providers.DependenciesContainer()
    )

    health_check_get = providers.Factory(
        CheckHealth,
        health_check_service=services.health_service,
    )
