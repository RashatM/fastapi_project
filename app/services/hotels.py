from datetime import date
from typing import Optional, List


from app.interfaces.repositories.hotels import IHotelRepository
from app.interfaces.services.hotels import IHotelService
from app.interfaces.uow import IUnitOfWork
from app.exceptions.hotel_exceptions import HotelIsNotExistsException
from app.dto.hotels import HotelDTO, HotelInfoDTO
from app.utils.booking_dates_validators import validate_filter_dates


class HotelService(IHotelService):

    def __init__(self,  uow: IUnitOfWork, hotel_repository: IHotelRepository) -> None:
        self.uow = uow
        self.hotel_repository = hotel_repository

    async def get_hotel_by_id(self, hotel_id: int) -> Optional[HotelDTO]:
        hotel: Optional[HotelDTO] = await self.hotel_repository.find_hotel_by_id(hotel_id=hotel_id)
        if not hotel:
            raise HotelIsNotExistsException(hotel_id)
        return hotel

    async def get_hotels_by_location_and_date(
        self,
        location: str,
        date_from: date,
        date_to: date
    ) -> List[HotelInfoDTO]:
        validate_filter_dates(date_from, date_to)

        return await self.hotel_repository.find_all_hotels_by_location_and_date(
            location=location,
            date_from=date_from,
            date_to=date_to
        )

