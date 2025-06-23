from typing import Dict, cast

from services.health import HealthCheckService


class CheckGetHealth:
    """
    Use case for checking the health of the application.
    This use case is used to verify that the application is running and healthy.
    """

    def __init__(self, health_check_service: HealthCheckService):
        """
        Initialize the CheckGetHealth use case.
        """
        self.health_check_service = health_check_service

    def execute(self) -> Dict[str, str]:
        """
        Execute the health check.

        Returns:
            dict: A dictionary containing the health status.
        """
        return cast(Dict[str, str], self.health_check_service.check_health())
