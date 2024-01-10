from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker


from app.db.uow import UnitOfWork
from app.dependencies.stub import Stub


async def provide_session(pool: async_sessionmaker = Depends(Stub(async_sessionmaker[AsyncSession]))) -> AsyncSession:
    async with pool() as session:
        yield session


def provide_uow(session: AsyncSession = Depends(Stub(AsyncSession))) -> UnitOfWork:
    return UnitOfWork(session=session)



