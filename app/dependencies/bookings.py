from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.rooms import RoomRepository
from app.dependencies.stubs import uow_provider, session_provider, booking_repository_provider, room_repository_provider
from app.db.repositories.bookings import BookingRepository
from app.services.bookings import BookingService
from app.db.unit_of_work.uow import UnitOfWork


def provide_booking_repository(session: AsyncSession = Depends(session_provider)) -> BookingRepository:
    return BookingRepository(session=session)


def get_booking_service(
        uow: UnitOfWork = Depends(uow_provider),
        booking_repository: BookingRepository = Depends(booking_repository_provider),
        room_repository: RoomRepository = Depends(room_repository_provider)
) -> BookingService:
    return BookingService(uow=uow, booking_repository=booking_repository, room_repository=room_repository)
