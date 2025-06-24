from functools import lru_cache

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class ProjectSettings(BaseSettings):
    """
    Class to manage project configuration.
    Loads variables from a .env file.
    """

    PROJECT_NAME: str
    PROJECT_DESCRIPTION: str
    ENVIRONMENT: str

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> ProjectSettings:
    """
    Creates and returns an instance of ProjectSettings.
    Uses lru_cache to ensure the instance is a singleton (created only once).
    """
    try:
        return ProjectSettings()  # type: ignore
    except ValidationError as e:
        raise ValueError(f"Invalid project settings: {e}") from e


settings = get_settings()
