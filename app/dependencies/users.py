from typing import Optional

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.auth_adapter import AuthenticationAdapter
from app.adapters.encrypt_adapter import EncryptionAdapter
from app.db.uow import UnitOfWork
from app.dependencies.stubs import session_provider, uow_provider, user_repository_provider, auth_provider, \
    encrypt_provider
from app.exceptions.auth_exceptions import TokenAbsentException
from app.db.repositories.users import UserRepository
from app.dto.auth import UserPrivateDTO
from app.services.auth import AuthenticationService


def provide_user_repository(session: AsyncSession = Depends(session_provider)) -> UserRepository:
    return UserRepository(session=session)


def get_auth_service(
        uow: UnitOfWork = Depends(uow_provider),
        user_repository: UserRepository = Depends(user_repository_provider),
        authentication_provider: AuthenticationAdapter = Depends(auth_provider),
        encrypt_adapter: EncryptionAdapter = Depends(encrypt_provider)
) -> AuthenticationService:
    return AuthenticationService(
        uow=uow,
        user_repository=user_repository,
        auth_adapter=authentication_provider,
        encrypt_adapter=encrypt_adapter
    )


def get_token(request: Request) -> str:
    token = request.cookies.get("booking_access_token")
    if not token:
        raise TokenAbsentException
    return token


async def get_current_user(
        token: str = Depends(get_token),
        auth_service: AuthenticationService = Depends(get_auth_service)
) -> Optional[UserPrivateDTO]:
    return await auth_service.verify_token(token=token)
