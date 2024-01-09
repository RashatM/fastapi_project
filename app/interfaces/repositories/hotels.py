from abc import abstractmethod, ABC
from datetime import date
from typing import Optional, List


from app.dto.hotels import HotelDTO, HotelInfoDTO


class IHotelRepository(ABC):

    @abstractmethod
    async def find_hotel_by_id(self, hotel_id: int) -> Optional[HotelDTO]:
        pass

    @abstractmethod
    async def find_all_hotels_by_location_and_date(
        self,
        location: str,
        date_from: date,
        date_to: date
    ) -> List[HotelInfoDTO]:
        pass







