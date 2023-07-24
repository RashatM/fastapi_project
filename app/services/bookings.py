from datetime import date
from typing import List

from app.db.repositories.rooms import RoomRepository
from app.db.unit_of_work.uow import UnitOfWork
from app.db.repositories.bookings import BookingRepository
from app.exceptions.room_exceptions import RoomIsNotExistsException, NotAvailableRoomsException
from app.schemas.bookings import BookingSchema, BookingInfoSchema
from app.schemas.rooms import RoomSchema


class BookingService:

    def __init__(
        self,
        uow: UnitOfWork,
        booking_repository: BookingRepository,
        room_repository: RoomRepository
    ):
        self.uow = uow
        self.booking_repository = booking_repository
        self.room_repository = room_repository

    async def get_bookings_by_user(self, user_id: int) -> List[BookingInfoSchema]:
        return await self.booking_repository.find_bookings_by_user_id(user_id=user_id)

    async def add_new_booking(
        self,
        room_id: int,
        user_id: int,
        date_from: date,
        date_to: date
    ) -> BookingSchema:

        exist_room: RoomSchema = await self.room_repository.get_exist_room(room_id=room_id)

        if not exist_room:
            raise RoomIsNotExistsException

        exist_booking: BookingSchema = await self.booking_repository.get_exist_booking(
            room_id=room_id,
            date_from=date_from,
            date_to=date_to
        )

        if exist_booking:
            new_booking: BookingSchema = await self.booking_repository.add_booking(
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






