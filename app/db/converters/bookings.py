import sqlalchemy
from sqlalchemy.engine.row import RowMapping, Row


from app.db.models.bookings import BookingModel
from app.schemas.bookings import NewBookingSchema, BookingInfoSchema, UnbookedRoomsInfoSchema


def convert_db_model_to_new_booking_dto(booking: BookingModel) -> NewBookingSchema:
    return NewBookingSchema(
        room_id=booking.room_id,
        user_id=booking.user_id,
        date_from=booking.date_from,
        date_to=booking.date_to,
        price=booking.price,
        total_cost=booking.total_cost,
        total_days=booking.total_days
    )


def convert_db_model_to_booking_info_dto(booking_info: RowMapping) -> BookingInfoSchema:
    return BookingInfoSchema(
        room_id=booking_info.room_id,
        user_id=booking_info.user_id,
        date_from=booking_info.date_from,
        date_to=booking_info.date_to,
        price=booking_info.price,
        total_cost=booking_info.total_cost,
        total_days=booking_info.total_days,
        image_id=booking_info.image_id,
        name=booking_info.name,
        description=booking_info.description,
        services=booking_info.services
    )


def convert_db_model_to_unbooked_rooms_info_dto(room: Row) -> UnbookedRoomsInfoSchema:
    return UnbookedRoomsInfoSchema(
        rooms_left_count=room.rooms_left_count,
        price=room.price
    )

