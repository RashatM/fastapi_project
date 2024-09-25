from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.config import settings


def create_pool(database_url: str, echo_mode: bool) -> async_sessionmaker:
    engine = create_async_engine(
        database_url,
        echo=echo_mode
    )
    session = async_sessionmaker(
        bind=engine,
        autocommit=False,
        expire_on_commit=False,
        autoflush=False
    )
    return session


class Base(DeclarativeBase):
    pass



