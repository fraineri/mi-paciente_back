from typing import Dict

from core.settings.project_settings import ProjectSettings


class HealthCheckService:
    """
    Service for checking the health of the application.
    This service is used to verify that the application is running and healthy.
    """

    def __init__(self, project_settings: ProjectSettings):
        """
        Initialize the HealthCheckService.
        """
        self.project_settings = project_settings

    def check_health(self) -> Dict[str, str]:
        """
        Check the health of the application.

        Returns:
            dict: A dictionary containing the health status.
        """
        return {
            "status": "healthy",
            "project_name": self.project_settings.PROJECT_NAME,
            "environment": self.project_settings.ENVIRONMENT,
        }
