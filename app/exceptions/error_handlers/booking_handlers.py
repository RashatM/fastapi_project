from fastapi.responses import ORJSONResponse
from fastapi import status
from fastapi.requests import Request

from app.exceptions.booking_exceptions import NotExistsBookingsByUserException, DateFromCannotBeAfterDateToException, \
    DatesCannotBeLessThanCurrentDayException, DatePeriodMoreThanOneYearException, CannotBookHotelForLongPeriodException
from app.exceptions.error_handlers.handlers import handle_error


async def not_exist_bookings_by_user_handler(request: Request, err: NotExistsBookingsByUserException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)


async def date_from_is_greater_than_date_to_handler(
    request: Request,
    err: DateFromCannotBeAfterDateToException
) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)


async def exceeding_date_of_current_day_handler(
    request: Request,
    err: DatesCannotBeLessThanCurrentDayException
) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)


async def exceeding_date_period_handler(request: Request, err: DatePeriodMoreThanOneYearException) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)


async def too_long_booking_period_handler(
    request: Request,
    err: CannotBookHotelForLongPeriodException
) -> ORJSONResponse:
    return await handle_error(request, err, status_code=status.HTTP_409_CONFLICT)





