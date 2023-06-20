from typing import Dict, TypeVar

from sqlalchemy import delete, insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from app.database import Base

BaseModel = TypeVar("BaseModel", bound=Base)


class BaseRepository:

    def __init__(self, model: type[BaseModel], session: AsyncSession):
        self._model = model
        self._session = session

    async def find_one_or_none(self, **filter_by):
        query = select(self._model.__table__.columns).filter_by(**filter_by)
        result = await self._session.execute(query)
        return result.one_or_none()

    async def find_all(self, **filter_by):
        query = select(self._model.__table__.columns).filter_by(**filter_by)
        result = await self._session.execute(query)
        return result.mappings().all()

    async def add(self, **data):
        query = insert(self._model).values(**data).returning(self._model.id)
        result = await self._session.execute(query)
        return result.mappings().first()

