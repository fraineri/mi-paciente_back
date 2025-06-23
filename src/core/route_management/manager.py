from typing import List

from fastapi import FastAPI

from core.route_management.router import VersionedAPIRouter


class RouteManager:
    """
    A class to manage the VersionedAPIRouters created and apply them to a FastAPI application.
    """

    class Route:
        def __init__(self, router: VersionedAPIRouter):
            self.router = router

    def __init__(self):
        self.routers: List[RouteManager.Route] = []

    def include_router(self, router: VersionedAPIRouter):
        self.routers.append(RouteManager.Route(router))

    def apply_routes(self, app: FastAPI):
        for router in self.routers:
            app.include_router(router.router)


route_manager = RouteManager()
