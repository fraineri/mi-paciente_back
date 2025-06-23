from dependency_injector.wiring import inject
from fastapi import status

from core.route_management.decorators import route
from core.route_management.enums import RouteVisibility
from core.route_management.router import VersionedAPIRouter, create_versioned_router

router: VersionedAPIRouter = create_versioned_router(path="/health")


@router.get(path="", status_code=status.HTTP_200_OK)
@route(visibility=RouteVisibility.PUBLIC, version=(1, 0))
@inject
async def ping():
    return {"status": "ok"}
