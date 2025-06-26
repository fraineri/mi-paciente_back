from sqlalchemy.orm import Mapped, mapped_column

from core.persistance.base_model import BaseModel


class UserModel(BaseModel):
    """ORM model for the User entity."""

    __tablename__ = "users"

    # Define additional fields specific to the User entity
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    password_hash: Mapped[str] = mapped_column(nullable=False)

    def __repr__(self):
        return f"<UserModel(id={self.id}, email={self.email})>"
