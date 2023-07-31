from dataclasses import dataclass

from app.exceptions.app_exception import AppException


@dataclass
class NotExistsBookingsByUserException(AppException):
    user_id: int

    @property
    def message(self) -> str:
        return f"У пользователя с id {self.user_id} отсутствуют бронирования"


@dataclass
class DateFromCannotBeAfterDateToException(AppException):

    @property
    def message(self) -> str:
        return f"Дата начала бронирования не может быть больше даты окончания бронирования"


@dataclass
class DatesCannotBeLessThanCurrentDayException(AppException):

    @property
    def message(self) -> str:
        return f"Даты бронирования не могут быть меньше сегодняшнего дня"


@dataclass
class DatePeriodMoreThanOneYearException(AppException):

    @property
    def message(self) -> str:
        return f"Период просмотра дат бронирования не может превышать одного года"


@dataclass
class CannotBookHotelForLongPeriodException(AppException):

    @property
    def message(self) -> str:
        return f"Нельзя забронировать номер более, чем на 31 день"