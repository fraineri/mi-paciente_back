from fastapi import FastAPI

from core.dependency_injection.container import Container
from core.route_management.manager import route_manager
from health.entry_points import health


class RouterSetup:

    def init(self, _app: FastAPI, container: Container):
        # Routes initialization
        route_manager.include_router(health.router)
        route_manager.apply_routes(_app)

        # Middlewares initialization
        # ....

        # Dependency injection
        container.wire(
            modules=[
                health,
            ]
        )


router_setup = RouterSetup()
