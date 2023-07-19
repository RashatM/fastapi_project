from datetime import date
from sqlalchemy import select, and_, func

from app.db.converters.bookings import convert_db_model_to_booking_dto
from app.db.models.rooms import RoomModel
from app.db.repositories.base import BaseRepository
from app.db.models.bookings import BookingModel
from app.schemas.bookings import BookingSchema


class BookingRepository(BaseRepository):

    async def get_price_by_room_id(self, room_id: int) -> int:
        price_query = select(RoomModel.price).filter(RoomModel.id == room_id)
        return await self._session.scalar(price_query)

    async def get_rooms_left_count(
        self,
        room_id: int,
        date_from: date,
        date_to: date
    ) -> int:
        """
            WITH booked_rooms AS (
                SELECT * FROM bookings
                WHERE 1=1
                AND room_id = 1
                AND (date_from <= '2023-06-20' AND date_to >= '2023-05-15')
            )
        """

        booked_rooms = (
            select(BookingModel)
            .where(
                and_(
                    BookingModel.room_id == 1,
                    and_(
                        BookingModel.date_from <= date_to,
                        BookingModel.date_to >= date_from
                    )
                )
            )
        ).cte("booked_rooms")

        """
            SELECT rooms.quantity - COUNT(booked_rooms.room_id)
            FROM rooms
            LEFT JOIN booked_rooms ON booked_rooms.room_id = rooms.id
            WHERE rooms.id = 1
            GROUP BY rooms.quantity, booked_rooms.room_id
        """

        rooms_left_count_query = (
            select(RoomModel.quantity - func.count(booked_rooms.c.room_id))
            .select_from(RoomModel)
            .join(booked_rooms, booked_rooms.c.room_id == RoomModel.id, isouter=True)
            .where(RoomModel.id == room_id)
            .group_by(RoomModel.quantity, booked_rooms.c.room_id)
        )

        rooms_left_count: int = await self._session.scalar(rooms_left_count_query)
        return rooms_left_count

    async def add_booking(
        self,
        room_id: int,
        user_id: int,
        date_from: date,
        date_to: date
    ) -> BookingSchema:
        price: int = await self.get_price_by_room_id(room_id=room_id)

        new_booking = BookingModel(
            room_id=room_id,
            user_id=user_id,
            date_from=date_from,
            date_to=date_to,
            price=price
        )
        self._session.add(new_booking)
        await self._session.flush()

        return convert_db_model_to_booking_dto(new_booking)
