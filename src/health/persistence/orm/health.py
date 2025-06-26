from sqlalchemy.orm import Mapped, mapped_column

from core.persistance.base_model import BaseModel


class HealthModel(BaseModel):
    """ORM model for the Health entity."""

    __tablename__ = "health"

    app_name: Mapped[str] = mapped_column(
        primary_key=True, index=True, unique=True, nullable=False
    )
    status: Mapped[str] = mapped_column(nullable=False)
    message: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"<HealthModel(app_name={self.app_name}, status={self.status}, message={self.message})>"
