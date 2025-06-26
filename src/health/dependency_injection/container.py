from dependency_injector import containers, providers

from health.dependency_injection.containers.persistance import PersistanceContainer
from health.dependency_injection.containers.services import ServicesContainer
from health.dependency_injection.containers.usecases import UseCasesContainer


class HealthContainer(containers.DeclarativeContainer):
    core_settings = providers.DependenciesContainer()
    core_persistance = providers.DependenciesContainer()
    core_clients = providers.DependenciesContainer()
    core_services = providers.DependenciesContainer()

    persistance = providers.Container(
        PersistanceContainer,
        core_persistance=core_persistance,
        core_clients=core_clients,
    )

    services = providers.Container(
        ServicesContainer,
        core_settings=core_settings,
        persistance=persistance,
    )

    usecases = providers.Container(UseCasesContainer, services=services)
