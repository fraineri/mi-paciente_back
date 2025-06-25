from functools import lru_cache

from pydantic import ValidationError
from pydantic_settings import BaseSettings, SettingsConfigDict


class RedisSettings(BaseSettings):
    """
    Class to manage Redis configuration.
    Loads variables from a .env file.
    """

    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int

    @property
    def redis_url(self) -> str:
        """
        Returns the Redis connection URL.
        """
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


@lru_cache
def get_settings() -> RedisSettings:
    """
    Creates and returns an instance of RedisSettings.
    Uses lru_cache to ensure the instance is a singleton (created only once).
    """
    try:
        return RedisSettings()  # type: ignore
    except ValidationError as e:
        raise ValueError(f"Invalid Redis settings: {e}") from e


settings = get_settings()
