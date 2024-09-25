from sqlalchemy.ext.asyncio import AsyncSession


from app.interfaces.uow import IUnitOfWork


class UnitOfWork(IUnitOfWork):

    def __init__(self, session: AsyncSession):
        self._session = session

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

