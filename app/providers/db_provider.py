from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.unit_of_work.uow import UnitOfWork


def uow_provider():
    raise NotImplementedError


class DBProvider:
    def __init__(self, pool: async_sessionmaker):
        self.pool = pool

    async def provide_db(self):
        async with self.pool() as session:
            yield UnitOfWork(session)
