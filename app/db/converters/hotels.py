from sqlalchemy import Row

from app.db.models.hotels import HotelModel
from app.schemas.hotels import HotelSchema, HotelInfoSchema


def convert_db_model_to_hotel_dto(hotel: HotelModel) -> HotelSchema:
    return HotelSchema(
        id=hotel.id,
        name=hotel.name,
        location=hotel.location,
        services=hotel.services,
        rooms_quantity=hotel.rooms_quantity,
        image_id=hotel.image_id
    )


def convert_db_model_to_hotel_info_dto(hotel_info: Row) -> HotelInfoSchema:
    return HotelInfoSchema(
        id=hotel_info.id,
        name=hotel_info.name,
        location=hotel_info.location,
        services=hotel_info.services,
        rooms_quantity=hotel_info.rooms_quantity,
        image_id=hotel_info.image_id,
        rooms_left_count=hotel_info.rooms_left_count
    )

