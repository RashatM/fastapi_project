from abc import abstractmethod, ABC
from datetime import date
from typing import Optional, List


from app.dto.rooms import RoomDTO, RoomInfoDTO


class IRoomRepository(ABC):
    @abstractmethod
    async def find_exist_room(self, room_id: int) -> Optional[RoomDTO]:
        pass

    async def find_all_rooms_by_hotel_and_date(
            self,
            hotel_id: int,
            date_from: date,
            date_to: date
    ) -> List[RoomInfoDTO]:
        pass
