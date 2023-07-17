from fastapi import FastAPI

from app.exceptions.error_handlers.handlers import *


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(UserAlreadyExistsException, user_already_exist_handler)
    app.add_exception_handler(UserIsNotExistsException, user_is_not_exist_handler)
    app.add_exception_handler(UserIsNotAuthorizedException, user_is_not_authorized_handler)
    app.add_exception_handler(UserIsNotPresentException, user_is_not_present_handler)
    app.add_exception_handler(TokenAbsentException, token_absent_handler)
    app.add_exception_handler(IncorrectTokenFormatException, incorrect_token_handler)
