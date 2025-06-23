from dependency_injector import containers, providers

from core.settings.database_settings import DatabaseSettings


class CoreSettingsContainer(containers.DeclarativeContainer):
    database_settings: providers.Singleton[DatabaseSettings] = providers.Singleton(
        DatabaseSettings
    )
