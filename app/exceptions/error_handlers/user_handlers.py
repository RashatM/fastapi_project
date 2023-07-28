from fastapi.responses import ORJSONResponse
from fastapi import status
from fastapi.requests import Request

from app.exceptions.auth_exceptions import *
from app.exceptions.error_handlers.handlers import handle_error


async def user_already_exist_handler(request: Request, err: UserAlreadyExistsException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)


async def user_is_not_exist_handler(request: Request, err: UserIsNotExistsException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_401_UNAUTHORIZED)


async def user_is_not_authorized_handler(request: Request, err: UserIsNotAuthorizedException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_401_UNAUTHORIZED)


async def user_is_not_present_handler(request: Request, err: UserIsNotPresentException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_401_UNAUTHORIZED)


async def token_absent_handler(request: Request, err: TokenAbsentException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_401_UNAUTHORIZED)


async def incorrect_token_handler(request: Request, err: IncorrectTokenFormatException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_401_UNAUTHORIZED)


async def expired_token_handler(request: Request, err: TokenExpiredException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_401_UNAUTHORIZED)