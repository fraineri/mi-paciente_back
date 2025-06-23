from typing import Any, Callable, Tuple, TypeVar

from core.route_management.enums import RouteVisibility

F = TypeVar("F", bound=Callable[..., Any])


def route(
    visibility: RouteVisibility, version: Tuple[int, int] = (1, 0)
) -> Callable[[F], F]:
    """
    Decorator to mark a route as internal or public and specify its version.
    ...
    """
    if not isinstance(visibility, RouteVisibility):
        raise ValueError(
            f"Invalid visibility: {visibility}. Must be a RouteVisibility enum value."
        )

    if not isinstance(version, tuple):
        raise ValueError(f"Invalid version: {version}. Must be a tuple.")

    def decorator(func: F) -> F:
        """
        Attaches routing information to the function object.
        """
        # We use setattr to dynamically add attributes to the function object.
        # This is a clean way to handle this without Mypy complaining about
        # missing attributes on the generic function type 'F'.
        # We disable the Ruff warning B010 because in this specific case,
        # using setattr is a deliberate choice to work around a static typing limitation.
        setattr(func, "internal", visibility == RouteVisibility.INTERNAL)  # noqa: B010
        setattr(func, "version", version)  # noqa: B010
        return func

    return decorator
