from dataclasses import dataclass

from app.exceptions.app_exception import AppException


@dataclass
class UserAlreadyExistsException(AppException):

    @property
    def message(self):
        return "Такой пользователь уже существует"


@dataclass
class UserIsNotAuthorizedException(AppException):

    @property
    def message(self) -> str:
        return "Пользователь не авторизован"


@dataclass
class TokenAbsentException(AppException):

    @property
    def message(self) -> str:
        return "Токен отсутствует"
