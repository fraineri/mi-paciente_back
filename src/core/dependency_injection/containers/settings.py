from dependency_injector import containers, providers

from core.settings.postgres_settings import PostgresSettings
from core.settings.project_settings import ProjectSettings


class SettingsContainer(containers.DeclarativeContainer):
    project_settings: providers.Singleton[ProjectSettings] = providers.Singleton(
        ProjectSettings
    )
    postgres_settings: providers.Singleton[PostgresSettings] = providers.Singleton(
        PostgresSettings
    )
