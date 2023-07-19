from app.db.models.bookings import BookingModel
from app.schemas.bookings import BookingSchema


def convert_db_model_to_booking_dto(user: BookingModel) -> BookingSchema:
    return BookingSchema(
        room_id=user.room_id,
        user_id=user.user_id,
        date_from=user.date_from,
        date_to=user.date_to,
        price=user.price,
        total_cost=user.total_cost,
        total_days=user.total_days
    )