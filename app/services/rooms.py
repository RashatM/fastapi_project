from datetime import date
from typing import Optional, List

from app.interfaces.repositories.hotels import IHotelRepository
from app.interfaces.repositories.rooms import IRoomRepository
from app.interfaces.services.rooms import IRoomService
from app.interfaces.uow import IUnitOfWork
from app.exceptions.hotel_exceptions import HotelIsNotExistsException
from app.dto.hotels import HotelDTO
from app.dto.rooms import RoomInfoDTO
from app.utils.booking_dates_validators import validate_filter_dates


class RoomService(IRoomService):

    def __init__(self, uow: IUnitOfWork, room_repository: IRoomRepository, hotel_repository: IHotelRepository):
        self.uow = uow
        self.room_repository = room_repository
        self.hotel_repository = hotel_repository

    async def get_rooms_by_hotel_id_and_date(
            self,
            hotel_id: int,
            date_from: date,
            date_to: date
    ) -> List[RoomInfoDTO]:
        validate_filter_dates(date_from, date_to)

        exist_hotel: Optional[HotelDTO] = await self.hotel_repository.find_hotel_by_id(hotel_id=hotel_id)

        if not exist_hotel:
            raise HotelIsNotExistsException(hotel_id)

        return await self.room_repository.find_all_rooms_by_hotel_and_date(
            hotel_id=hotel_id,
            date_from=date_from,
            date_to=date_to
        )
