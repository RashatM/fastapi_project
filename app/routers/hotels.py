from datetime import date, datetime, timedelta
from typing import Optional, List, Annotated
from fastapi import APIRouter, Query, Depends

from app.dependencies.stub import Stub
from app.dto.hotels import HotelDTO, HotelInfoDTO
from app.dto.rooms import RoomInfoDTO
from app.interfaces.services.hotels import IHotelService
from app.interfaces.services.rooms import IRoomService

hotel_router = APIRouter(
    prefix="/hotels",
    tags=["Отели"]
)


@hotel_router.get("/{location}")
async def get_hotels_by_location_and_time(
        location: str,
        date_from: Annotated[date, Query(..., description=f"Например, {datetime.now().date()}")],
        date_to: Annotated[date, Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}")],
        service: Annotated[IHotelService, Depends(Stub(IHotelService))]
) -> List[HotelInfoDTO]:
    return await service.get_hotels_by_location_and_date(
        location=location,
        date_from=date_from,
        date_to=date_to
    )



@hotel_router.get("/id/{hotel_id}")
async def get_hotel_by_id(
        hotel_id: int,
        service: Annotated[IHotelService, Depends(Stub(IHotelService))]
) -> Optional[HotelDTO]:
    return await service.get_hotel_by_id(hotel_id=hotel_id)


@hotel_router.get("/{hotel_id}/rooms")
async def get_rooms_by_hotel_and_time(
    hotel_id: int,
    date_from: Annotated[date, Query(..., description=f"Например, {datetime.now().date()}")],
    date_to: Annotated[date, Query(..., description=f"Например, {(datetime.now() + timedelta(days=14)).date()}")],
    service: Annotated[IRoomService, Depends(Stub(IRoomService))]
) -> List[RoomInfoDTO]:
    return await service.get_rooms_by_hotel_id_and_date(
        hotel_id=hotel_id,
        date_from=date_from,
        date_to=date_to
    )
