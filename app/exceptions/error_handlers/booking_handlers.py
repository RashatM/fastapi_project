from fastapi.responses import ORJSONResponse
from fastapi import status
from fastapi.requests import Request

from app.exceptions.booking_exceptions import NotExistsBookingsByUserException
from app.exceptions.error_handlers.handlers import handle_error


async def not_exist_bookings_by_user_handler(request: Request, err: NotExistsBookingsByUserException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)
