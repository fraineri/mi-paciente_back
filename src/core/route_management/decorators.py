from functools import update_wrapper
from typing import Any, Callable, Generic, Tuple, TypeVar

from core.route_management.enums import RouteVisibility

F = TypeVar("F", bound=Callable[..., Any])


class Routable(Generic[F]):
    """
    A wrapper for a callable that includes routing information.
    """

    def __init__(self, func: F, visibility: RouteVisibility, version: Tuple[int, int]):
        if not isinstance(visibility, RouteVisibility):
            raise ValueError(
                f"Invalid visibility: {visibility}. Must be a RouteVisibility enum value."
            )

        if not isinstance(version, tuple):
            raise ValueError(f"Invalid version: {version}. Must be a tuple.")

        self.callable = func
        self.internal = visibility == RouteVisibility.INTERNAL
        self.version = version

        update_wrapper(self, func)

    # El método __call__ DEBE ser 'async' y usar 'await'
    async def __call__(self, *args: Any, **kwargs: Any) -> Any:
        """
        When the Routable instance is called, it executes the underlying async function.
        """
        return await self.callable(*args, **kwargs)


def route(
    visibility: RouteVisibility, version: Tuple[int, int] = (1, 0)
) -> Callable[[F], Routable[F]]:
    """
    Decorator to mark a route as internal or public and specify its version.

    Args:
        visibility (RouteVisibility): The visibility of the route.
        version (Tuple[int, int]): The API version for this route as a tuple of (major, minor). Defaults to (1, 0).

    Returns:
        Callable: A decorator that wraps the function in a Routable object.
    """

    def decorator(func: F) -> Routable[F]:
        return Routable(func, visibility, version)

    return decorator
