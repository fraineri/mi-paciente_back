from redis.asyncio.client import Redis

from core.persistance.connection_managers.redis import RedisConnectionManager


class RedisClient:
    def __init__(self, redis_connection_manager: RedisConnectionManager):
        self.redis_conn: Redis = redis_connection_manager.get_connection()

    async def get(self, key) -> str | None:
        """
        Get the value of a key from Redis.
        Args:
            key (str): The key to retrieve.
        Returns:
            str | None: The value associated with the key, or None if the key does not exist.
        """

        value = await self.redis_conn.get(key)
        if value is not None:
            return value.decode("utf-8") if isinstance(value, bytes) else str(value)
        return None

    async def set(self, key, value, ex=None):
        """
        Set a key-value pair in Redis with an optional expiration time.

        Args:
            key (str): The key to set.
            value (str): The value to set.
            ex (int, optional): Expiration time in seconds. Defaults to None.
        """
        return await self.redis_conn.set(key, value, ex=ex)

    async def delete(self, key):
        """
        Delete a key from Redis.

        Args:
            key (str): The key to delete.
        """
        return await self.redis_conn.delete(key)
