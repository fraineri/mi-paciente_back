from pydantic import BaseModel


class Health(BaseModel):
    """Domain model for the Health entity."""

    app_name: str
    status: str
    message: str

    def __repr__(self) -> str:
        return f"<Health(app_name={self.app_name}, status={self.status}, message={self.message})>"
