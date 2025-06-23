from typing import Dict


class HealthCheckService:
    """
    Service for checking the health of the application.
    This service is used to verify that the application is running and healthy.
    """

    def __init__(self):
        """
        Initialize the HealthCheckService.
        """
        pass

    def check_health(self) -> Dict[str, str]:
        """
        Check the health of the application.

        Returns:
            dict: A dictionary containing the health status.
        """
        return {"status": "healthy"}
