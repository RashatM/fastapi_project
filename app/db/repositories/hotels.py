from datetime import date
from typing import Optional, List
from sqlalchemy import select, and_, func

from app.db.converters.hotels import convert_db_model_to_hotel_dto, convert_db_model_to_hotel_info_dto
from app.db.models.bookings import BookingModel
from app.db.models.hotels import HotelModel
from app.db.models.rooms import RoomModel
from app.db.repositories.base import BaseRepository
from app.schemas.hotels import HotelSchema, HotelInfoSchema


class HotelRepository(BaseRepository):

    async def find_hotel_by_id(self, hotel_id: int) -> Optional[HotelSchema]:
        query = select(HotelModel).filter(HotelModel.id == hotel_id)
        result = await self._session.execute(query)
        hotel: Optional[HotelModel] = result.scalar_one_or_none()

        if hotel:
            return convert_db_model_to_hotel_dto(hotel=hotel)
        return None

    async def find_all_hotels_by_location_and_date(
        self,
        location: str,
        date_from: date,
        date_to: date
    ) -> List[HotelInfoSchema]:

        booked_rooms = (
            select(BookingModel.room_id)
            .where(
                and_(
                    BookingModel.date_from <= date_to,
                    BookingModel.date_to >= date_from
                )
            )
            .cte("booked_rooms")
        )

        free_rooms = (
            select(RoomModel.hotel_id, func.count(RoomModel.id).label("rooms_left_count"))
            .select_from(RoomModel)
            .join(booked_rooms, booked_rooms.c.room_id == RoomModel.id, isouter=True)
            .where(booked_rooms.c.room_id.is_(None))
            .group_by(RoomModel.hotel_id)
            .cte("free_rooms")
        )

        hotels_with_free_rooms_query = (
            select(
                HotelModel.__table__.columns,
                free_rooms.c.rooms_left_count
            )
            .join(free_rooms, free_rooms.c.hotel_id == HotelModel.id)
            .where(func.lower(HotelModel.location).like(f"%{location.lower()}%"))
        )

        result = await self._session.execute(hotels_with_free_rooms_query)
        hotels = result.mappings().all()

        if hotels:
            return [convert_db_model_to_hotel_info_dto(hotel_info) for hotel_info in hotels]
        return []







