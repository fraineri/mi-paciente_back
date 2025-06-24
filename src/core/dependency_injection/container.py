from dependency_injector import containers, providers

from core.dependency_injection.containers.services import ServicesContainer
from core.dependency_injection.containers.settings import SettingsContainer
from core.dependency_injection.containers.usecases import UseCasesContainer


class Container(containers.DeclarativeContainer):
    settings = providers.Container(SettingsContainer)
    services = providers.Container(ServicesContainer, settings=settings)
    usecases = providers.Container(UseCasesContainer, services=services)
