import time

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class BaseModel(DeclarativeBase):
    """Base model for all database tables."""

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
