from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlalchemy.orm import DeclarativeBase


def create_engine(database_url: str, echo_mode: bool) -> AsyncEngine:
    engine = create_async_engine(
        database_url,
        echo=echo_mode
    )
    return engine


def create_pool(engine: AsyncEngine) -> async_sessionmaker:
    session = async_sessionmaker(
        bind=engine,
        autocommit=False,
        expire_on_commit=False,
        autoflush=False
    )
    return session


class Base(DeclarativeBase):
    pass







