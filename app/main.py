import uvicorn
from fastapi import FastAPI

from app.db.database import create_pool
from app.dependencies import setup_di
from app.exceptions.error_handlers import setup_exception_handlers
from app.routers import setup_routes
from app.config import settings


def build_app() -> FastAPI:
    """Factory application"""

    app = FastAPI()
    pool = create_pool(database_url=settings.DATABASE_URL, echo_mode=True)

    # setup application
    setup_di(
        app=app,
        pool=pool
    )
    setup_routes(app=app)
    setup_exception_handlers(app=app)

    return app


if __name__ == "__main__":
    uvicorn.run(app="main:build_app", host="127.0.0.1", port=8000, reload=True)






