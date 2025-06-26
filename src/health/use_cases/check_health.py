from health.domain.health import Health
from health.services.health import HealthCheckService


class CheckHealth:
    """
    Use case for checking the health of the application.
    This use case is used to verify that the application is running and healthy.
    """

    def __init__(self, health_check_service: HealthCheckService):
        self.health_check_service = health_check_service

    async def execute(self) -> Health:
        """
        Execute the health check.

        Returns:
            Health: An instance of Health containing the health status.
        Raises:
            ValueError: If the health check fails and no health data is returned.
        """
        health = await self.health_check_service.check_health()

        if not health:
            raise ValueError("Health check failed, no health data returned.")

        return health
