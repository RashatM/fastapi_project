from datetime import date, datetime, timedelta
from typing import Optional, List

from fastapi import APIRouter, Query, Depends

from app.dependencies.hotels import get_hotel_service
from app.dependencies.rooms import get_room_service
from app.schemas.hotels import HotelSchema, HotelInfoSchema
from app.schemas.rooms import RoomInfoSchema
from app.services.hotels import HotelService
from app.services.rooms import RoomService

hotel_router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@hotel_router.get("/{location}")
async def get_hotels_by_location_and_time(
        location: str,
        date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
        date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
        service: HotelService = Depends(get_hotel_service)
) -> List[HotelInfoSchema]:
    return await service.get_hotels_by_location_and_date(
        location=location,
        date_from=date_from,
        date_to=date_to
    )


@hotel_router.get("/id/{hotel_id}")
async def get_hotel_by_id(hotel_id: int, service: HotelService = Depends(get_hotel_service)) -> Optional[HotelSchema]:
    return await service.get_hotel_by_id(hotel_id=hotel_id)


@hotel_router.get("/{hotel_id}/rooms")
async def get_rooms_by_hotel_and_time(
    hotel_id: int,
    date_from: date = Query(..., description=f"Например, {datetime.now().date()}"),
    date_to: date = Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}"),
    service: RoomService = Depends(get_room_service)
) -> List[RoomInfoSchema]:
    return await service.get_rooms_by_hotel_id_and_date(
        hotel_id=hotel_id,
        date_from=date_from,
        date_to=date_to
    )
