from dependency_injector import containers, providers

from core.dependency_injection.containers.settings import CoreSettingsContainer


class Container(containers.DeclarativeContainer):
    core_settings = providers.Container(CoreSettingsContainer)
