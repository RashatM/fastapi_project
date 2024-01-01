from datetime import date
from typing import List

from app.db.repositories.rooms import RoomRepository
from app.db.unit_of_work.uow import UnitOfWork
from app.db.repositories.bookings import BookingRepository
from app.exceptions.booking_exceptions import NotExistsBookingsByUserException
from app.exceptions.room_exceptions import RoomIsNotExistsException, NotAvailableRoomsException
from app.dto.bookings import BookingDTO, BookingInfoDTO
from app.dto.rooms import RoomDTO
from app.utils.booking_dates_validators import validate_filter_dates, validate_booking_dates


class BookingService:

    def __init__(
        self,
        uow: UnitOfWork,
        booking_repository: BookingRepository,
        room_repository: RoomRepository
    ) -> None:
        self.uow = uow
        self.booking_repository = booking_repository
        self.room_repository = room_repository

    async def get_bookings_by_user(self, user_id: int) -> List[BookingInfoDTO]:
        bookings: List[BookingInfoDTO] = await self.booking_repository.find_bookings_by_user_id(user_id=user_id)
        if not bookings:
            raise NotExistsBookingsByUserException(user_id)
        return bookings

    async def add_new_booking(
            self,
            room_id: int,
            user_id: int,
            date_from: date,
            date_to: date
    ) -> BookingDTO:

        validate_filter_dates(date_from, date_to)
        validate_booking_dates(date_from, date_to)

        exist_room: RoomDTO = await self.room_repository.find_exist_room(room_id=room_id)

        if not exist_room:
            raise RoomIsNotExistsException(room_id)

        exist_booking: BookingDTO = await self.booking_repository.find_exist_booking(
            room_id=room_id,
            date_from=date_from,
            date_to=date_to
        )

        if not exist_booking:
            new_booking: BookingDTO = await self.booking_repository.add_booking(
                room_id=room_id,
                user_id=user_id,
                date_from=date_from,
                date_to=date_to,
                price=exist_room.price
            )
            await self.uow.commit()
        else:
            raise NotAvailableRoomsException

        return new_booking

    async def remove_booking_by_id(self, booking_id: int, user_id: int):
        await self.booking_repository.delete_booking_by_id(
            booking_id=booking_id,
            user_id=user_id
        )
        await self.uow.commit()
