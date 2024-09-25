from fastapi import FastAPI

from app.exceptions.auth import UserAlreadyExistsException
from app.exceptions.error_handlers.handlers import user_already_exist_handler


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(UserAlreadyExistsException, user_already_exist_handler)



