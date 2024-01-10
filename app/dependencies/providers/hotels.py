from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.hotels import HotelRepository
from app.dependencies.stub import Stub
from app.interfaces.repositories.hotels import IHotelRepository
from app.interfaces.uow import IUnitOfWork
from app.services.hotels import HotelService


def provide_hotel_repository(session: AsyncSession = Depends(Stub(AsyncSession))) -> HotelRepository:
    return HotelRepository(session=session)


def provide_hotel_service(
        uow: IUnitOfWork = Depends(Stub(IUnitOfWork)),
        hotel_repository: IHotelRepository = Depends(Stub(IHotelRepository))
) -> HotelService:
    return HotelService(uow=uow, hotel_repository=hotel_repository)
