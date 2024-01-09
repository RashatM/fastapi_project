from datetime import date
from typing import List
from abc import ABC, abstractmethod

from app.dto.rooms import RoomInfoDTO


class IRoomService(ABC):

    @abstractmethod
    async def get_rooms_by_hotel_id_and_date(
            self,
            hotel_id: int,
            date_from: date,
            date_to: date
    ) -> List[RoomInfoDTO]:
        pass
