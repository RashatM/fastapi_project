from fastapi import Depends, Request

from app.providers.db_provider import uow_provider
from app.services.auth import UserService
from app.unit_of_work.uow import UnitOfWork


def get_user_service(uow: UnitOfWork = Depends(uow_provider)) -> UserService:
    return UserService(uow=uow)


def get_token(request: Request) -> str:
    return request.cookies.get("booking_access_token")


def get_current_user(token: str = Depends(get_token)):
    pass
