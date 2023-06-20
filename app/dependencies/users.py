from fastapi import Depends

from app.providers.db import uow_provider
from app.services.auth import UserService
from app.unit_of_work.uow import UnitOfWork


def get_user_service(uow: UnitOfWork = Depends(uow_provider)) -> UserService:
    return UserService(uow=uow)


def get_current_user(user_service: UserService = Depends(get_user_service)):
    pass
