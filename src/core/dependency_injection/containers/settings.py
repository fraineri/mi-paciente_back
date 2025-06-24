from dependency_injector import containers, providers

from core.settings.database_settings import DatabaseSettings
from core.settings.project_settings import ProjectSettings


class SettingsContainer(containers.DeclarativeContainer):
    project_settings: providers.Singleton[ProjectSettings] = providers.Singleton(
        ProjectSettings
    )
    database_settings: providers.Singleton[DatabaseSettings] = providers.Singleton(
        DatabaseSettings
    )
