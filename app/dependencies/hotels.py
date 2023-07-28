from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.hotels import HotelRepository
from app.dependencies.stubs import uow_provider, session_provider, hotel_repository_provider
from app.db.unit_of_work.uow import UnitOfWork
from app.services.hotels import HotelService


def provide_hotel_repository(session: AsyncSession = Depends(session_provider)) -> HotelRepository:
    return HotelRepository(session=session)


def get_hotel_service(
        uow: UnitOfWork = Depends(uow_provider),
        hotel_repository: HotelRepository = Depends(hotel_repository_provider)
) -> HotelService:
    return HotelService(uow=uow, hotel_repository=hotel_repository)
