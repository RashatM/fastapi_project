from datetime import date
from typing import Optional, List
from abc import ABC, abstractmethod


from app.dto.hotels import HotelDTO, HotelInfoDTO


class IHotelService(ABC):

    @abstractmethod
    async def get_hotel_by_id(self, hotel_id: int) -> Optional[HotelDTO]:
        pass

    @abstractmethod
    async def get_hotels_by_location_and_date(
        self,
        location: str,
        date_from: date,
        date_to: date
    ) -> List[HotelInfoDTO]:
        pass

