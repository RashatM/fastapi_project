from datetime import date
from typing import Optional, List

from app.db.repositories.hotels import HotelRepository
from app.db.unit_of_work.uow import UnitOfWork
from app.exceptions.hotel_exceptions import HotelIsNotExistsException
from app.schemas.hotels import HotelSchema, HotelInfoSchema


class HotelService:

    def __init__(self,  uow: UnitOfWork, hotel_repository: HotelRepository) -> None:
        self.uow = uow
        self.hotel_repository = hotel_repository

    async def get_hotel_by_id(self, hotel_id: int) -> Optional[HotelSchema]:
        hotel: Optional[HotelSchema] = await self.hotel_repository.find_hotel_by_id(hotel_id=hotel_id)
        if not hotel:
            raise HotelIsNotExistsException(hotel_id)
        return hotel

    async def get_hotels_by_location_and_date(
        self,
        location: str,
        date_from: date,
        date_to: date
    ) -> List[HotelInfoSchema]:
        return await self.hotel_repository.find_all_hotels_by_location_and_date(
            location=location,
            date_from=date_from,
            date_to=date_to
        )

