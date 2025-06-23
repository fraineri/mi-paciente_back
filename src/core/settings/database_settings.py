# src/core/config.py
from functools import lru_cache

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseSettings(BaseSettings):
    """
    Class to manage database configuration.
    Loads variables from a .env file.
    """

    POSTGRES_USER: str
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_HOST: str
    POSTGRES_PORT: int

    @property
    def database_url(self) -> str:
        """
        Returns the database connection URL.
        """
        return f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> DatabaseSettings:
    """
    Crea y retorna una instancia de DatabaseSettings.
    Utiliza lru_cache para asegurar que la instancia sea un singleton (se crea una sola vez).
    """
    try:
        return DatabaseSettings()  # type: ignore
    except ValidationError as e:
        raise ValueError(f"Invalid database settings: {e}") from e


settings = get_settings()
