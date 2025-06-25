import time
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """Base model for all database tables."""

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        index=True,
        default=uuid.uuid4,
        unique=True,
        nullable=False,
    )
    created_at: Mapped[int] = mapped_column(
        default=lambda: int(time.time()),
        nullable=False,
    )
    updated_at: Mapped[int] = mapped_column(
        default=lambda: int(time.time()),
        onupdate=lambda: int(time.time()),
        nullable=False,
    )
    deleted_at: Mapped[int | None] = mapped_column(
        default=None,
        nullable=True,
    )
