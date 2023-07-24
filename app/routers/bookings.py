from typing import List

from fastapi import APIRouter, Depends, status


from app.dependencies.bookings import get_booking_service
from app.dependencies.users import get_current_user
from app.schemas.auth import UserPrivateSchema
from app.schemas.bookings import BookingRequestSchema, BookingSchema, BookingInfoSchema
from app.services.bookings import BookingService

booking_router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@booking_router.get("")
async def get_bookings(
    user: UserPrivateSchema = Depends(get_current_user),
    service: BookingService = Depends(get_booking_service)
) -> List[BookingInfoSchema]:
    return await service.get_bookings_by_user(user_id=user.id)


@booking_router.post("", status_code=status.HTTP_201_CREATED)
async def add_booking(
    booking_data: BookingRequestSchema,
    user: UserPrivateSchema = Depends(get_current_user),
    service: BookingService = Depends(get_booking_service)
) -> BookingSchema:
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
    user: UserPrivateSchema = Depends(get_current_user),
    service: BookingService = Depends(get_booking_service)
):
    await service.remove_booking_by_id(
        booking_id=booking_id,
        user_id=user.id
    )

