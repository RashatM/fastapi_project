from abc import abstractmethod, ABC
from datetime import date
from typing import List, Optional


from app.dto.bookings import BookingDTO, BookingInfoDTO


class IBookingRepository(ABC):

    @abstractmethod
    async def find_bookings_by_user_id(self, user_id: int) -> List[BookingInfoDTO]:
        pass

    @abstractmethod
    async def find_exist_booking(
            self,
            room_id: int,
            date_from: date,
            date_to: date
    ) -> Optional[BookingDTO]:
        pass

    @abstractmethod
    async def add_booking(
            self,
            room_id: int,
            user_id: int,
            date_from: date,
            date_to: date,
            price: int
    ) -> BookingDTO:
        pass

    @abstractmethod
    async def delete_booking_by_id(self, booking_id: int, user_id: int):
        pass
