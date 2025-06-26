from typing import Optional

from core.settings.project_settings import ProjectSettings
from health.domain.health import Health
from health.persistence.repositories.health_repository import HealthRepository


class HealthCheckService:
    """
    Service for checking the health of the application.
    This service is used to verify that the application is running and healthy.
    """

    def __init__(
        self, project_settings: ProjectSettings, health_repository: HealthRepository
    ):
        """
        Initialize the HealthCheckService.
        """
        self.project_settings = project_settings
        self.health_repository = health_repository

    async def check_health(self) -> Optional[Health]:
        """
        Check the health of the application.

        Returns:
            dict: A dictionary containing the health status.
        """
        return Health(
            app_name=self.project_settings.PROJECT_NAME,
            status="healthy",
            message="The application is running smoothly.",
        )

    async def create_health(self, health_data: dict) -> Health:
        """
        Create a new health status for the application.
        Args:
            health_data (dict): A dictionary containing the health status data.
        Returns:
            Health: An instance of Health containing the created health status.
        """
        health = Health(
            app_name=self.project_settings.PROJECT_NAME,
            status=health_data.get("status", "unknown"),
            message=health_data.get("message", "No message provided."),
        )
        return await self.health_repository.save(health)

    async def update_health(self, health_data: dict) -> Health:
        """
        Update the health status of the application.
        Args:
            health_data (dict): A dictionary containing the health status data.
        Returns:
            Health: An instance of Health containing the updated health status.
        """
        health = Health(
            app_name=self.project_settings.PROJECT_NAME,
            status=health_data.get("status", "unknown"),
            message=health_data.get("message", "No message provided."),
        )
        return await self.health_repository.update(health)
