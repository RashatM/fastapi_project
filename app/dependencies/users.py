from typing import Optional

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.adapters.encrypt_adapter import EncryptionAdapter
from app.dependencies.stubs import session_provider, uow_provider, user_repository_provider, auth_provider, \
    encrypt_provider

from app.exceptions.auth_exceptions import TokenAbsentException
from app.providers.auth_provider import AuthenticationProvider
from app.db.repositories.users import UserRepository
from app.schemas.auth import UserPrivateSchema
from app.services.auth import AuthenticationService
from app.db.unit_of_work.uow import UnitOfWork


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
) -> Optional[UserPrivateSchema]:
    return await auth_service.verify_token(token=token)
