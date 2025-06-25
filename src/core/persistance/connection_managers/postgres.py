from sqlalchemy.ext.asyncio import (
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from core.settings.postgres_settings import PostgresSettings


class PostgresConnectionManager:
    def __init__(self, postgres_settings: PostgresSettings):
        # Engine y Session Factory for writing
        self._write_engine = create_async_engine(postgres_settings.database_url_write)
        self._write_session_maker = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._write_engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

        # Engine y Session Factory for reading
        self._read_engine = create_async_engine(postgres_settings.database_url_read)
        self._read_session_maker = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._read_engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    def get_write_session_factory(self) -> async_sessionmaker[AsyncSession]:
        """
        Returns the session factory for writing operations.
        This session is bound to the write engine.
        """
        return self._write_session_maker

    def get_read_session_factory(self) -> async_sessionmaker[AsyncSession]:
        """
        Returns the session factory for reading operations.
        This session is bound to the read engine.
        """
        return self._read_session_maker
