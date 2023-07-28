from dataclasses import dataclass

from app.exceptions.app_exception import AppException


@dataclass
class NotExistsBookingsByUserException(AppException):
    user_id: int

    @property
    def message(self) -> str:
        return f"У пользователя с id {self.user_id} отсутсвуют бронирования"