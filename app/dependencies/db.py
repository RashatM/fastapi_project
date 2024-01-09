from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.stubs import session_provider
from app.db.uow import UnitOfWork


def provide_uow(session: AsyncSession = Depends(session_provider)) -> UnitOfWork:
    return UnitOfWork(session=session)