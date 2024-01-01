from typing import List
from pydantic import BaseModel


class HotelDTO(BaseModel):
    id: int
    name: str
    location: str
    services: List[str]
    rooms_quantity: int
    image_id: int


class HotelInfoDTO(HotelDTO):
    rooms_left_count: int

