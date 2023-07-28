from fastapi.responses import ORJSONResponse
from fastapi import status
from fastapi.requests import Request

from app.exceptions.error_handlers.handlers import handle_error
from app.exceptions.room_exceptions import NotAvailableRoomsException, RoomIsNotExistsException


async def room_fully_booked_handler(request: Request, err: NotAvailableRoomsException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)


async def room_is_not_exists_booked_handler(request: Request, err: RoomIsNotExistsException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)