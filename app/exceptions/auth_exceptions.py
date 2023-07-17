from dataclasses import dataclass

from app.exceptions.app_exception import AppException


@dataclass
class UserAlreadyExistsException(AppException):

    @property
    def message(self):
        return "Такой пользователь уже существует"


@dataclass
class UserIsNotExistsException(AppException):

    @property
    def message(self):
        return "Пользователь с данным логином и паролем не существует"


@dataclass
class UserIsNotPresentException(AppException):

    @property
    def message(self) -> str:
        return "Не установлен пользователь в токене"


@dataclass
class UserIsNotPresentException(AppException):

    @property
    def message(self) -> str:
        return "Не установлен пользователь в токене"


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


@dataclass
class IncorrectTokenFormatException(AppException):

    @property
    def message(self) -> str:
        return "Неверный формат токена"
