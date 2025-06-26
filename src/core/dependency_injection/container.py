from dependency_injector import containers, providers

from core.dependency_injection.containers.clients import CoreClientsContainer
from core.dependency_injection.containers.persistance import CorePersistanceContainer
from core.dependency_injection.containers.services import CoreServicesContainer
from core.dependency_injection.containers.settings import CoreSettingsContainer
from health.dependency_injection.container import HealthContainer


class Container(containers.DeclarativeContainer):
    core_settings = providers.Container(CoreSettingsContainer)
    core_persistance = providers.Container(
        CorePersistanceContainer, settings=core_settings
    )
    core_clients = providers.Container(
        CoreClientsContainer,
        core_settings=core_settings,
        core_persistance=core_persistance,
    )
    core_services = providers.Container(
        CoreServicesContainer, persistance=core_persistance, settings=core_settings
    )

    health: providers.Container[HealthContainer] = providers.Container(
        HealthContainer,
        core_settings=core_settings,
        core_persistance=core_persistance,
        core_clients=core_clients,
        core_services=core_services,
    )
