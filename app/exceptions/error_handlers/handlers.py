from fastapi.responses import ORJSONResponse
from fastapi import status
from fastapi.requests import Request

from app.exceptions.app_exception import AppException
from app.exceptions.error_handlers.error_result import ErrorResult


async def unknown_exception_handler(request: Request, err: Exception) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(message="Unknown server error has occurred", data=err),
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )


async def handle_error(request: Request, err: AppException, status_code: int) -> ORJSONResponse:
    return ORJSONResponse(
        ErrorResult(message=err.message, data=err),
        status_code=status_code,
    )






