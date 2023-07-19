from datetime import date

from app.db.unit_of_work.uow import UnitOfWork
from app.db.repositories.bookings import BookingRepository
from app.exceptions.auth_exceptions import NotAvailableRoomsException
from app.schemas.bookings import BookingSchema


class BookingService:

    def __init__(self, uow: UnitOfWork, booking_repository: BookingRepository):
        self.uow = uow
        self.booking_repository = booking_repository

    async def add_new_booking(
        self,
        room_id: int,
        user_id: int,
        date_from: date,
        date_to: date
    ) -> BookingSchema:

        rooms_left_count: int = await self.booking_repository.get_rooms_left_count(
            room_id=room_id,
            date_from=date_from,
            date_to=date_to
        )

        if rooms_left_count > 0:
            new_booking = await self.booking_repository.add_booking(
                room_id=room_id,
                user_id=user_id,
                date_from=date_from,
                date_to=date_to
            )
            await self.uow.commit()
        else:
            raise NotAvailableRoomsException

        return new_booking




