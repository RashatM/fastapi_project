from dataclasses import dataclass

from app.exceptions.app_exception import AppException


@dataclass
class NotAvailableRoomsException(AppException):

    @property
    def message(self) -> str:
        return "Не осталось свободных номеров"


@dataclass
class RoomIsNotExistsException(AppException):
    room_id: int

    @property
    def message(self) -> str:
        return f"Номера с id {self.room_id} не существует"