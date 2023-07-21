from dataclasses import dataclass

from app.exceptions.app_exception import AppException


@dataclass
class NotAvailableRoomsException(AppException):

    @property
    def message(self) -> str:
        return "Не осталось свободных номеров"


@dataclass
class RoomIsNotExistsException(AppException):

    @property
    def message(self) -> str:
        return "Такого номера не существует"