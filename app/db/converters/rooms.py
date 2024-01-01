from sqlalchemy import RowMapping

from app.db.models.rooms import RoomModel
from app.dto.rooms import RoomDTO, RoomInfoDTO


def convert_db_model_to_room_dto(room: RoomModel) -> RoomDTO:
    return RoomDTO(
        id=room.id,
        hotel_id=room.hotel_id,
        name=room.name,
        description=room.description,
        price=room.price,
        services=room.services,
        quantity=room.quantity,
        image_id=room.image_id
    )


def convert_db_model_to_room_info_dto(room: RowMapping) -> RoomInfoDTO:
    return RoomInfoDTO(
        id=room.id,
        hotel_id=room.hotel_id,
        name=room.name,
        description=room.description,
        price=room.price,
        services=room.services,
        quantity=room.quantity,
        image_id=room.image_id,
        total_cost= room.total_cost,
        rooms_left_count=room.rooms_left_count
    )

