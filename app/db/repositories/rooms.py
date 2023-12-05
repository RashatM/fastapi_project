from datetime import date
from operator import and_
from typing import Optional, List
from sqlalchemy import select, func, and_

from app.db.converters.rooms import convert_db_model_to_room_dto, convert_db_model_to_room_info_dto
from app.db.models.bookings import BookingModel
from app.db.models.hotels import HotelModel
from app.db.models.rooms import RoomModel
from app.db.repositories.base import BaseRepository
from app.schemas.rooms import RoomSchema, RoomInfoSchema


class RoomRepository(BaseRepository):

    async def find_exist_room(self, room_id: int) -> Optional[RoomSchema]:
        query = select(RoomModel).filter(RoomModel.id == room_id)
        exist_room = await self._session.scalar(query)

        if exist_room:
            return convert_db_model_to_room_dto(room=exist_room)

    async def find_all_rooms_by_hotel_and_date(
        self,
        hotel_id: int,
        date_from: date,
        date_to: date
    ) -> List[RoomInfoSchema]:

        booked_rooms = (
            select(BookingModel.room_id, func.count(BookingModel.room_id).label("rooms_booked_count"))
            .where(
                and_(
                    BookingModel.date_from <= date_to,
                    BookingModel.date_to >= date_from
                )
            )
            .group_by(BookingModel.room_id)
            .cte("booked_rooms")
        )

        free_rooms_query = (
            select(
                RoomModel.__table__.columns,
                (RoomModel.price * (date_to - date_from).days).label("total_cost"),
                (HotelModel.rooms_quantity - func.coalesce(booked_rooms.c.rooms_booked_count, 0))
                .label("rooms_left_count")
            )
            .join(booked_rooms, booked_rooms.c.room_id == RoomModel.id, isouter=True)
            .join(HotelModel, HotelModel.id == RoomModel.hotel_id)
            .where(RoomModel.hotel_id == hotel_id)
        )

        result = await self._session.execute(free_rooms_query)
        rooms = result.mappings().all()

        if rooms:
            return [convert_db_model_to_room_info_dto(room_info) for room_info in rooms]
        return []

