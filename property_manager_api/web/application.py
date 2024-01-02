import logging

from fastapi import FastAPI
from fastapi.responses import UJSONResponse
from property_manager_api.settings import settings
from property_manager_api.web.api.router import api_router
from importlib import metadata

from property_manager_api.web.lifetime import (register_shutdown_event,
                                                        register_startup_event)
from property_manager_api.logging import configure_logging
from pathlib import Path

from fastapi.staticfiles import StaticFiles

APP_ROOT = Path(__file__).parent.parent


def get_app() -> FastAPI:
    """
    Get FastAPI application.

    This is the main constructor of an application.

    :return: application.
    """
    configure_logging()
    app = FastAPI(
        title="Property Manager API",
        version=metadata.version("property_manager_api"),
        docs_url=None,
        redoc_url=None,
        
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse,
    )

    # Adds startup and shutdown events.
    register_startup_event(app)
    register_shutdown_event(app)

    # Main router for the API.
    app.include_router(router=api_router, prefix="/api")
    # Adds static directory.
    # This directory is used to access swagger files.
    app.mount(
        "/static",
        StaticFiles(directory=APP_ROOT / "static"),
        name="static"
    )
    

    return app
