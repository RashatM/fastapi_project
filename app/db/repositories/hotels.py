from datetime import date
from typing import Optional, List
from sqlalchemy import select, and_, func

from app.db.converters.hotels import convert_db_model_to_hotel_dto, convert_db_model_to_hotel_info_dto
from app.db.models.bookings import BookingModel
from app.db.models.hotels import HotelModel
from app.db.models.rooms import RoomModel
from app.db.repositories.base import BaseRepository
from app.dto.hotels import HotelDTO, HotelInfoDTO
from app.interfaces.repositories.hotels import IHotelRepository


class HotelRepository(BaseRepository, IHotelRepository):

    async def find_hotel_by_id(self, hotel_id: int) -> Optional[HotelDTO]:
        query = select(HotelModel).filter(HotelModel.id == hotel_id)
        result = await self._session.execute(query)
        hotel: Optional[HotelModel] = result.scalar_one_or_none()

        if hotel:
            return convert_db_model_to_hotel_dto(hotel=hotel)

    async def find_all_hotels_by_location_and_date(
        self,
        location: str,
        date_from: date,
        date_to: date
    ) -> List[HotelInfoDTO]:

        available_rooms = (
            select(RoomModel.hotel_id, func.count(RoomModel.id).label("rooms_left_count"))
            .filter(
                ~RoomModel.booking.has(
                    and_(
                        BookingModel.date_from <= date_to,
                        BookingModel.date_to >= date_from
                    )
                )
            )
            .group_by(RoomModel.hotel_id)
            .cte("available_rooms")
        )

        # Получаем отели с доступными комнатами и количеством оставшихся комнат
        hotels_with_free_rooms_query = (
            select(HotelModel.__table__.columns, available_rooms.c.rooms_left_count)
            .select_from(HotelModel)
            .join(available_rooms, available_rooms.c.hotel_id == HotelModel.id) 
            .filter(HotelModel.location.like(f"%{location}%"))
        )

        result = await self._session.execute(hotels_with_free_rooms_query)
        hotels = result.all()

        if hotels:
            return [convert_db_model_to_hotel_info_dto(hotel_info) for hotel_info in hotels]
        return []







