from datetime import date
from typing import List, Optional
from sqlalchemy import select, and_, delete


from app.db.converters.bookings import convert_db_model_to_booking_dto, convert_db_model_to_booking_info_dto
from app.db.models.rooms import RoomModel
from app.db.repositories.base import BaseRepository
from app.db.models.bookings import BookingModel
from app.schemas.bookings import BookingSchema, BookingInfoSchema


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
        bookings = result.all()

        if bookings:
            return [convert_db_model_to_booking_info_dto(booking_info) for booking_info in bookings]
        return []

    async def find_exist_booking(
            self,
            room_id: int,
            date_from: date,
            date_to: date
    ) -> Optional[BookingSchema]:
        booked_rooms_query = (
            select(BookingModel)
            .where(
                and_(
                    BookingModel.room_id == room_id,
                    and_(
                        BookingModel.date_from <= date_to,
                        BookingModel.date_to >= date_from
                    )
                )
            )
        )

        result = await self._session.execute(booked_rooms_query)
        booked_room: Optional[BookingModel] = result.one_or_none()
        
        if booked_room:
            return convert_db_model_to_booking_dto(booked_room)

    async def add_booking(
            self,
            room_id: int,
            user_id: int,
            date_from: date,
            date_to: date,
            price: int
    ) -> BookingSchema:
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

    async def delete_booking_by_id(self, booking_id: int, user_id: int):
        query = (
            delete(BookingModel)
            .filter(
                and_(
                    BookingModel.id == booking_id,
                    BookingModel.user_id == user_id
                )
            )
        )
        await self._session.execute(query)

