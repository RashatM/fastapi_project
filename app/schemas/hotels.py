from typing import List
from pydantic import BaseModel


class HotelSchema(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int


class HotelInfoSchema(HotelSchema):
    rooms_left_count: int

