from app.db.models.rooms import RoomModel
from app.schemas.rooms import RoomSchema


def convert_db_model_to_room_dto(room: RoomModel) -> RoomSchema:
    return RoomSchema(
        id=room.id,
        hotel_id=room.hotel_id,
        name=room.name,
        description=room.description,
        price=room.price,
        services=room.services,
        quantity=room.quantity,
        image_id=room.image_id
    )
