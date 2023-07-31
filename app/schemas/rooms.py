from typing import List

from pydantic import BaseModel


class RoomSchema(BaseModel):
    id: int
    hotel_id: int
    name: str
    description: str
    price: int
    services: List[str]
    quantity: int
    image_id: int


class RoomInfoSchema(RoomSchema):
    total_cost: int
    rooms_left_count: int




