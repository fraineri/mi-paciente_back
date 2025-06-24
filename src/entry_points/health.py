from dependency_injector.wiring import Provide, inject
from fastapi import Depends, status

from core.dependency_injection.container import Container
from core.route_management.decorators import route
from core.route_management.enums import RouteVisibility
from core.route_management.router import VersionedAPIRouter, create_versioned_router
from use_cases.health.check_get_health import CheckGetHealth

router: VersionedAPIRouter = create_versioned_router(path="/health")


@router.get(path="/get", status_code=status.HTTP_200_OK)
@route(visibility=RouteVisibility.PUBLIC, version=(1, 0))
@inject
async def get_ping(
    check_get_health: CheckGetHealth = Depends(  # noqa: B008
        Provide[Container.usecases.health_check_get]
    ),
):
    return check_get_health.execute()
