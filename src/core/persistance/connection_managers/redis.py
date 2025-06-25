from typing import cast

import redis.asyncio as aioredis
from redis.asyncio.client import Redis
from redis.asyncio.connection import ConnectionPool

from core.settings.redis_settings import RedisSettings


class RedisConnectionManager:
    """
    Manages the asynchronous connection to Redis.
    """

    def __init__(self, settings: RedisSettings):
        self._pool: ConnectionPool = aioredis.ConnectionPool.from_url(
            settings.redis_url, decode_responses=True  # Decodificar respuestas a UTF-8
        )

    def get_connection(self) -> Redis:
        """
        Returns a Redis connection from the pool.
        """
        return cast(Redis, aioredis.Redis(connection_pool=self._pool))
