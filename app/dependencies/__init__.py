from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.providers.db_provider import DBProvider, uow_provider


def setup_di(app: FastAPI, pool: async_sessionmaker) -> None:
    db_provider = DBProvider(pool)

    app.dependency_overrides[uow_provider] = db_provider.provide_db
