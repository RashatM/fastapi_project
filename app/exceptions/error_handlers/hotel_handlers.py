from fastapi.responses import ORJSONResponse
from fastapi import status
from fastapi.requests import Request

from app.exceptions.error_handlers.handlers import handle_error
from app.exceptions.hotel_exceptions import HotelIsNotExistsException


async def hotel_is_not_exists_handler(request: Request, err: HotelIsNotExistsException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)
