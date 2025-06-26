from typing import Dict

from health.domain.health import Health
from health.services.health import HealthCheckService


class UpdateHealth:
    """
    Use case for updating the health of the application.
    This use case is used to save the health status of the application.
    """

    def __init__(self, health_check_service: HealthCheckService):
        self.health_check_service = health_check_service

    async def execute(self, health_data: Dict[str, str]) -> Health:
        """
        Execute  the health update.

        Returns:
            Health: An instance of Health containing the health status.
        """
        return await self.health_check_service.update_health(health_data)
