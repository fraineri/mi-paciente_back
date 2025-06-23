# src/core/database.py
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from core.settings.database_settings import settings


class PostgresConnectionManager:
    """
    Manages the PostgreSQL database connection asynchronously.
    """

    def __init__(self, db_url: str):
        """
        Initializes the database engine and session maker.
        """
        self._engine = create_async_engine(db_url)
        self._session_maker = async_sessionmaker(
            autocommit=False,
            autoflush=False,
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False,
        )

    async def get_db_session(self) -> AsyncGenerator[AsyncSession, None]:
        """
        Dependency generator that provides a database session
        and ensures it is properly closed.
        """
        async with self._session_maker() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise
            finally:
                await session.close()


db_manager = PostgresConnectionManager(settings.database_url)
