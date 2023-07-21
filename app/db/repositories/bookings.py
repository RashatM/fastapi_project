from datetime import date
from typing import List

from sqlalchemy import select, and_, func, delete

from app.db.converters.bookings import convert_db_model_to_new_booking_dto, convert_db_model_to_booking_info_dto, \
    convert_db_model_to_unbooked_rooms_info_dto
from app.db.models.rooms import RoomModel
from app.db.repositories.base import BaseRepository
from app.db.models.bookings import BookingModel
from app.schemas.bookings import NewBookingSchema, BookingInfoSchema, UnbookedRoomsInfoSchema


class BookingRepository(BaseRepository):

    async def find_bookings_by_user_id(self, user_id: int) -> List[BookingInfoSchema]:
        query = (
            select(
                BookingModel.room_id,
                BookingModel.user_id,
                BookingModel.date_from,
                BookingModel.date_to,
                BookingModel.price,
                BookingModel.total_cost,
                BookingModel.total_days,
                RoomModel.image_id,
                RoomModel.name,
                RoomModel.description,
                RoomModel.services
            )
            .join(RoomModel, BookingModel.room_id == RoomModel.id, isouter=True)
            .where(BookingModel.user_id == user_id)
        )
        result = await self._session.execute(query)
        data = result.mappings().all()

        return [convert_db_model_to_booking_info_dto(booking_info) for booking_info in data]

    async def get_price_by_room_id(self, room_id: int) -> int:
        price_query = select(RoomModel.price).filter(RoomModel.id == room_id)
        return await self._session.scalar(price_query)

    async def get_exist_room(self, room_id: int):
        query = select(RoomModel).filter(RoomModel.id == room_id)
        return await self._session.scalar(query)

    async def get_unbooked_rooms_info(
            self,
            room_id: int,
            date_from: date,
            date_to: date
    ) -> UnbookedRoomsInfoSchema:
        """
            WITH booked_rooms AS (
                SELECT bookings.room_id, count(bookings.room_id) as rooms_booked_count
                FROM bookings
                WHERE 1=1
                AND room_id = 1
                AND (date_from <= '2023-06-20' AND date_to >= '2023-05-15')
            )
        """

        booked_rooms = (
            select(BookingModel.room_id, func.count(BookingModel.room_id).label("rooms_booked_count"))
            .select_from(BookingModel)
            .where(
                and_(
                    BookingModel.room_id == room_id,
                    and_(
                        BookingModel.date_from <= date_to,
                        BookingModel.date_to >= date_from
                    )
                )
            )
            .group_by(BookingModel.room_id)
        ).cte("booked_rooms")

        """
            SELECT rooms.quantity - booked_rooms.rooms_booked_count
            FROM rooms
            LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
            WHERE rooms.id = 1
        """

        rooms_left_count_with_price_query = (
            select(
                (RoomModel.quantity - func.coalesce(booked_rooms.c.rooms_booked_count, 0)).label("rooms_left_count"),
                RoomModel.price
            )
            .select_from(RoomModel)
            .join(booked_rooms, booked_rooms.c.room_id == RoomModel.id, isouter=True)
            .where(RoomModel.id == room_id)
        )

        result = await self._session.execute(rooms_left_count_with_price_query)
        rooms_left_count_with_price = result.one_or_none()
        return convert_db_model_to_unbooked_rooms_info_dto(rooms_left_count_with_price)

    async def add_booking(
            self,
            room_id: int,
            user_id: int,
            date_from: date,
            date_to: date,
            price: int
    ) -> NewBookingSchema:
        new_booking = BookingModel(
            room_id=room_id,
            user_id=user_id,
            date_from=date_from,
            date_to=date_to,
            price=price
        )
        self._session.add(new_booking)
        await self._session.flush()

        return convert_db_model_to_new_booking_dto(new_booking)

    async def delete_booking_by_id(self, booking_id: int, user_id: int):
        query = (
            delete(BookingModel)
            .filter(
                and_(
                    BookingModel.id == booking_id,
                    BookingModel.user_id == user_id
                )
            )
            .returning(BookingModel.price, BookingModel.user_id)
        )
        await self._session.execute(query)

