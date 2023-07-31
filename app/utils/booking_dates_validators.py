from datetime import date

from app.exceptions.booking_exceptions import DateFromCannotBeAfterDateToException, \
    DatesCannotBeLessThanCurrentDayException, DatePeriodMoreThanOneYearException, CannotBookHotelForLongPeriodException


def validate_filter_dates(date_from: date, date_to: date) -> None:
    if date_from > date_to:
        raise DateFromCannotBeAfterDateToException

    if date_from <= date.today() or date_to <= date.today():
        raise DatesCannotBeLessThanCurrentDayException

    if (date_to - date_from).days > 365:
        raise DatePeriodMoreThanOneYearException


def validate_booking_dates(date_from: date, date_to: date) -> None:
    if (date_to - date_from).days > 31:
        raise CannotBookHotelForLongPeriodException


