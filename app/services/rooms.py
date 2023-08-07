from datetime import date
from typing import Optional, List

from app.db.repositories.hotels import HotelRepository
from app.db.repositories.rooms import RoomRepository
from app.db.unit_of_work.uow import UnitOfWork
from app.exceptions.hotel_exceptions import HotelIsNotExistsException
from app.schemas.hotels import HotelSchema
from app.schemas.rooms import RoomInfoSchema
from app.utils.booking_dates_validators import validate_filter_dates


class RoomService:

    def __init__(
        self,
        uow: UnitOfWork,
        room_repository: RoomRepository,
        hotel_repository: HotelRepository
    ):
        self.uow = uow
        self.room_repository = room_repository
        self.hotel_repository = hotel_repository

    async def get_rooms_by_hotel_id_and_date(
        self,
        hotel_id: int,
        date_from: date,
        date_to: date
    ) -> List[RoomInfoSchema]:
        validate_filter_dates(date_from, date_to)

        exist_hotel: Optional[HotelSchema] = await self.hotel_repository.find_hotel_by_id(hotel_id=hotel_id)

        if not exist_hotel:
            raise HotelIsNotExistsException(hotel_id)

        return await self.room_repository.find_all_rooms_by_hotel_and_date(
            hotel_id=hotel_id,
            date_from=date_from,
            date_to=date_to
        )



