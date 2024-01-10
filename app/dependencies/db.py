from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.dependencies.stubs import session_provider, async_sessionmaker_provider
from app.db.uow import UnitOfWork


async def provide_session(pool: async_sessionmaker = Depends(async_sessionmaker_provider)) -> AsyncSession:
    async with pool() as session:
        yield session


def provide_uow(session: AsyncSession = Depends(session_provider)) -> UnitOfWork:
    return UnitOfWork(session=session)



