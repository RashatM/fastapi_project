from sqlalchemy.ext.asyncio import async_sessionmaker



class DBProvider:
    def __init__(self, pool: async_sessionmaker):
        self.pool = pool

    async def provide_session(self):
        async with self.pool() as session:
            yield session
