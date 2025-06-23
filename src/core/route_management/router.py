from typing import Callable, List, Optional

from fastapi import APIRouter


class VersionedAPIRouter(APIRouter):
    """
    An extended version of FastAPI's APIRouter.
    This extension allows and supports versioning and separation of internal and public routes.
    """

    def __init__(self, *args, **kwargs):
        # Remove the prefix from the kwargs to avoid FastAPI's automatic prefixing
        self.original_prefix = kwargs.pop("prefix", "")
        kwargs["prefix"] = ""
        super().__init__(*args, **kwargs)

        self.internal_routes: List[dict] = []
        self.public_routes: List[dict] = []

    def add_api_route(self, path: str, endpoint: Callable, **kwargs) -> None:
        """
        Add an API route with versioning and internal/public distinction.

        This method overrides the parent APIRouter's add_api_route method to include
        version information and separate internal and public routes.

        Args:
            path (str): The URL path for the route.
            endpoint (Callable): The function to be called when the path is accessed.
            **kwargs: Additional keyword arguments for the route.

        Returns:
            None
        """
        is_internal = getattr(endpoint, "internal", False)
        version = getattr(endpoint, "version", (1, 0))

        version_str = f"v{version[0]}_{version[1]}"

        prefix = self.original_prefix.strip("/")
        path = path.strip("/")

        if is_internal:
            full_path = f"/{version_str}/api/internal/{path}".rstrip("/")
            if prefix:
                full_path = f"/{version_str}/api/internal/{prefix}/{path}".rstrip("/")
            self.internal_routes.append(
                {"path": full_path, "endpoint": endpoint, "kwargs": kwargs}
            )
        else:
            full_path = f"/{version_str}/api/{prefix}/{path}".rstrip("/")
            self.public_routes.append(
                {"path": full_path, "endpoint": endpoint, "kwargs": kwargs}
            )

        full_path = "/" + full_path.strip("/")

        super().add_api_route(full_path, endpoint, **kwargs)


def create_versioned_router(path: Optional[str] = "") -> VersionedAPIRouter:
    """
    Create a new VersionedAPIRouter with the given path.
    """
    return VersionedAPIRouter(prefix=path)
