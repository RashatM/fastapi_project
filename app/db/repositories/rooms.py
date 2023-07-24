from typing import Optional
from sqlalchemy import select

from app.db.converters.rooms import convert_db_model_to_room_dto
from app.db.models.rooms import RoomModel
from app.db.repositories.base import BaseRepository
from app.schemas.rooms import RoomSchema


class RoomRepository(BaseRepository):

    async def get_exist_room(self, room_id: int) -> Optional[RoomSchema]:
        query = select(RoomModel).filter(RoomModel.id == room_id)
        exist_room = await self._session.scalar(query)

        if exist_room:
            return convert_db_model_to_room_dto(room=exist_room)
        return None
