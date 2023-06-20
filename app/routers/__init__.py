from fastapi import FastAPI

from app.routers.auth import auth_router


def setup_routes(app: FastAPI):
    app.include_router(auth_router)
