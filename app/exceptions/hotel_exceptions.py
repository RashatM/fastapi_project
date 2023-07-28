from dataclasses import dataclass

from app.exceptions.app_exception import AppException


@dataclass
class HotelIsNotExistsException(AppException):
    hotel_id: int

    @property
    def message(self) -> str:
        return f"Отеля с id {self.hotel_id} не существует"
