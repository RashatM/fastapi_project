from typing import List, Annotated

from fastapi import APIRouter, Depends, status


from app.dependencies.providers.users import get_current_user
from app.dependencies.stub import Stub
from app.dto.auth import UserPrivateDTO
from app.dto.bookings import BookingInfoDTO, BookingDTO
from app.interfaces.services.bookings import IBookingService
from app.schemas.bookings import BookingRequestSchema


booking_router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@booking_router.get("")
async def get_bookings(
    user: Annotated[UserPrivateDTO, Depends(get_current_user)],
    service: Annotated[IBookingService, Depends(Stub(IBookingService))]
) -> List[BookingInfoDTO]:
    return await service.get_bookings_by_user(user_id=user.id)


@booking_router.post("", status_code=status.HTTP_201_CREATED)
async def add_booking(
    booking_data: BookingRequestSchema,
    user: Annotated[UserPrivateDTO, Depends(get_current_user)],
    service: Annotated[IBookingService, Depends(Stub(IBookingService))]
) -> BookingDTO:
    booking = await service.add_new_booking(
        user_id=user.id,
        room_id=booking_data.room_id,
        date_from=booking_data.date_from,
        date_to=booking_data.date_to
    )
    return booking


@booking_router.delete("/{booking_id}")
async def remove_booking(
    booking_id: int,
    user: Annotated[UserPrivateDTO, Depends(get_current_user)],
    service: Annotated[IBookingService, Depends(Stub(IBookingService))]
):
    await service.remove_booking_by_id(
        booking_id=booking_id,
        user_id=user.id
    )

