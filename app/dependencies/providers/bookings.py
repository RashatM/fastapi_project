from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.dependencies.stub import Stub
from app.db.repositories.bookings import BookingRepository
from app.interfaces.repositories.bookings import IBookingRepository
from app.interfaces.repositories.rooms import IRoomRepository
from app.interfaces.uow import IUnitOfWork
from app.services.bookings import BookingService


def provide_booking_repository(session: AsyncSession = Depends(Stub(AsyncSession))) -> BookingRepository:
    return BookingRepository(session=session)


def provide_booking_service(
        uow: IUnitOfWork = Depends(Stub(IUnitOfWork)),
        booking_repository: IBookingRepository = Depends(Stub(IBookingRepository)),
        room_repository: IRoomRepository = Depends(Stub(IRoomRepository))
) -> BookingService:
    return BookingService(
        uow=uow,
        booking_repository=booking_repository,
        room_repository=room_repository
    )
