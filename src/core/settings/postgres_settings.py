from functools import lru_cache

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class PostgresSettings(BaseSettings):
    """
    Class to manage database configuration.
    Loads variables from a .env file.
    """

    POSTGRES_USER_WRITE: str
    POSTGRES_PASSWORD_WRITE: str
    POSTGRES_HOST_WRITE: str
    POSTGRES_PORT_WRITE: int
    POSTGRES_DB_WRITE: str

    POSTGRES_USER_READ: str
    POSTGRES_PASSWORD_READ: str
    POSTGRES_HOST_READ: str
    POSTGRES_PORT_READ: int
    POSTGRES_DB_READ: str

    @property
    def database_url_write(self) -> str:
        """Constructs the database URL for the write replica."""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER_WRITE}:{self.POSTGRES_PASSWORD_WRITE}@"
            f"{self.POSTGRES_HOST_WRITE}:{self.POSTGRES_PORT_WRITE}/{self.POSTGRES_DB_WRITE}"
        )

    @property
    def database_url_read(self) -> str:
        """Constructs the database URL for the read replica."""
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER_READ}:{self.POSTGRES_PASSWORD_READ}@"
            f"{self.POSTGRES_HOST_READ}:{self.POSTGRES_PORT_READ}/{self.POSTGRES_DB_READ}"
        )

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> PostgresSettings:
    """
    Crea y retorna una instancia de DatabaseSettings.
    Utiliza lru_cache para asegurar que la instancia sea un singleton (se crea una sola vez).
    """
    try:
        return PostgresSettings()  # type: ignore
    except ValidationError as e:
        raise ValueError(f"Invalid database settings: {e}") from e


settings = get_settings()
