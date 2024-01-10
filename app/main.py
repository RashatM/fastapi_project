from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI

from app.db.database import create_pool, create_engine
from app.dependencies import setup_di
from app.exceptions.error_handlers import setup_exception_handlers
from app.routers import setup_routes
from app.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    engine = create_engine(database_url=settings.DATABASE_URL, echo_mode=True)
    pool = create_pool(engine=engine)

    app.state.engine = engine
    app.state.pool = pool

    yield

    await app.state.engine.dispose()
    del app.state.engine


def build_app() -> FastAPI:
    app = FastAPI(lifespan=lifespan)

    setup_routes(app=app)
    setup_di(app=app)
    setup_exception_handlers(app=app)

    return app


if __name__ == "__main__":
    uvicorn.run(app="main:build_app", host="127.0.0.1", port=8000, reload=True, factory=True)
