from sqlalchemy.ext.asyncio import AsyncSession


class BaseRepository:

    def __init__(self, session: AsyncSession):
        self._session = session

    # async def find_one_or_none(self, **filter_by):
    #     query = select(self._model.__table__.columns).filter_by(**filter_by)
    #     result = await self._session.execute(query)
    #     return result.one_or_none()
    #
    # async def find_all(self, **filter_by):
    #     query = select(self._model.__table__.columns).filter_by(**filter_by)
    #     result = await self._session.execute(query)
    #     return result.mappings().all()
    #
    # async def add(self, **data):
    #     query = insert(self._model).values(**data).returning(self._model.id)
    #     result = await self._session.execute(query)
    #     return result.mappings().first()

