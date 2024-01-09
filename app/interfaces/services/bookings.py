from datetime import date
from typing import List
from abc import ABC, abstractmethod


from app.dto.bookings import BookingDTO, BookingInfoDTO


class IBookingService(ABC):
    @abstractmethod
    async def get_bookings_by_user(self, user_id: int) -> List[BookingInfoDTO]:
        pass

    @abstractmethod
    async def add_new_booking(
            self,
            room_id: int,
            user_id: int,
            date_from: date,
            date_to: date
    ) -> BookingDTO:
        pass

    @abstractmethod
    async def remove_booking_by_id(self, booking_id: int, user_id: int):
        pass
