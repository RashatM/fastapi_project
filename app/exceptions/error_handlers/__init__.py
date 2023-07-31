from fastapi import FastAPI

from app.exceptions.auth_exceptions import TokenExpiredException, IncorrectTokenFormatException, TokenAbsentException, \
    UserIsNotPresentException, UserIsNotAuthorizedException, UserIsNotExistsException, UserAlreadyExistsException
from app.exceptions.booking_exceptions import NotExistsBookingsByUserException, \
    DatesCannotBeLessThanCurrentDayException, DatePeriodMoreThanOneYearException, CannotBookHotelForLongPeriodException, \
    DateFromCannotBeAfterDateToException
from app.exceptions.error_handlers.booking_handlers import not_exist_bookings_by_user_handler, \
    exceeding_date_of_current_day_handler, exceeding_date_period_handler, too_long_booking_period_handler, \
    date_from_is_greater_than_date_to_handler
from app.exceptions.error_handlers.hotel_handlers import hotel_is_not_exists_handler
from app.exceptions.error_handlers.room_handlers import room_fully_booked_handler, room_is_not_exists_booked_handler
from app.exceptions.error_handlers.user_handlers import user_already_exist_handler, user_is_not_exist_handler, \
    user_is_not_authorized_handler, user_is_not_present_handler, token_absent_handler, incorrect_token_handler, \
    expired_token_handler
from app.exceptions.hotel_exceptions import HotelIsNotExistsException
from app.exceptions.room_exceptions import RoomIsNotExistsException, NotAvailableRoomsException


def setup_exception_handlers(app: FastAPI) -> None:
    app.add_exception_handler(UserAlreadyExistsException, user_already_exist_handler)
    app.add_exception_handler(UserIsNotExistsException, user_is_not_exist_handler)
    app.add_exception_handler(UserIsNotAuthorizedException, user_is_not_authorized_handler)
    app.add_exception_handler(UserIsNotPresentException, user_is_not_present_handler)
    app.add_exception_handler(TokenAbsentException, token_absent_handler)
    app.add_exception_handler(IncorrectTokenFormatException, incorrect_token_handler)
    app.add_exception_handler(TokenExpiredException, expired_token_handler)
    app.add_exception_handler(NotAvailableRoomsException, room_fully_booked_handler)
    app.add_exception_handler(RoomIsNotExistsException, room_is_not_exists_booked_handler)
    app.add_exception_handler(HotelIsNotExistsException, hotel_is_not_exists_handler)
    app.add_exception_handler(NotExistsBookingsByUserException, not_exist_bookings_by_user_handler)
    app.add_exception_handler(DateFromCannotBeAfterDateToException, date_from_is_greater_than_date_to_handler)
    app.add_exception_handler(DatesCannotBeLessThanCurrentDayException, exceeding_date_of_current_day_handler)
    app.add_exception_handler(DatePeriodMoreThanOneYearException, exceeding_date_period_handler)
    app.add_exception_handler(CannotBookHotelForLongPeriodException, too_long_booking_period_handler)















