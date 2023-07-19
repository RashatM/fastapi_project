from fastapi import APIRouter, Depends, status


from app.dependencies.bookings import get_booking_service
from app.dependencies.users import get_current_user
from app.schemas.auth import UserPrivateSchema
from app.schemas.bookings import BookingRequestSchema, BookingSchema
from app.services.bookings import BookingService

booking_router = APIRouter(
    prefix="/bookings",
    tags=["Бронирования"],
)


@booking_router.post("", status_code=status.HTTP_201_CREATED)
async def get_bookings(
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
