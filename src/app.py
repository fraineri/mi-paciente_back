import uvicorn
from fastapi import FastAPI

from core.dependency_injection.container import Container
from router_setup import router_setup


def create_app() -> FastAPI:
    container = Container()
    _app = FastAPI()

    router_setup.init(_app, container)

    return _app


app = create_app()

# Otherwise, run the app in the local environment
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
