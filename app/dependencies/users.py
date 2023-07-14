from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.encrypt_adapter import EncryptionAdapter
from app.providers.auth_provider import AuthenticationProvider
from app.repositories.users import UserRepository
from app.services.auth import AuthenticationService
from app.unit_of_work.uow import UnitOfWork


def session_provider():
    raise NotImplementedError


def uow_provider():
    raise NotImplementedError


def user_repository_provider():
    raise NotImplementedError


def auth_provider():
    raise NotImplementedError


def encrypt_provider():
    raise NotImplementedError


def provide_uow(session: AsyncSession = Depends(session_provider)) -> UnitOfWork:
    return UnitOfWork(session=session)


def provide_user_repository(session: AsyncSession = Depends(session_provider)) -> UserRepository:
    return UserRepository(session=session)


def get_auth_service(
        uow: UnitOfWork = Depends(uow_provider),
        user_repository: UserRepository = Depends(user_repository_provider),
        authentication_provider: AuthenticationProvider = Depends(auth_provider),
        encrypt_adapter: EncryptionAdapter = Depends(encrypt_provider)
) -> AuthenticationService:
    return AuthenticationService(
        uow=uow,
        user_repository=user_repository,
        auth_provider=authentication_provider,
        encrypt=encrypt_adapter
    )


def get_token(request: Request) -> str:
    return request.cookies.get("booking_access_token")


def get_current_user(token: str = Depends(get_token)):
    pass
