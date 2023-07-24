from typing import Optional, List
from pydantic import BaseModel
from datetime import date


class BookingSchema(BaseModel):
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int


class BookingRequestSchema(BaseModel):
    room_id: int
    date_from: date
    date_to: date


class BookingInfoSchema(BaseModel):
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int
    image_id: int
    name: str
    description: Optional[str]
    services: List[str]
