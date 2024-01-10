from typing import Optional

from fastapi import Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession

from app.dependencies.stub import Stub
from app.exceptions.auth_exceptions import TokenAbsentException
from app.db.repositories.users import UserRepository
from app.dto.auth import UserPrivateDTO
from app.interfaces.adapters.encrypt_adapter import IEncryptionAdapter
from app.interfaces.auth_adapter import IAuthenticationAdapter
from app.interfaces.repositories.users import IUserRepository
from app.interfaces.services.auth import IAuthenticationService
from app.interfaces.uow import IUnitOfWork
from app.services.auth import AuthenticationService


def provide_user_repository(session: AsyncSession = Depends(Stub(AsyncSession))) -> UserRepository:
    return UserRepository(session=session)


def provide_auth_service(
        uow: IUnitOfWork = Depends(Stub(IUnitOfWork)),
        user_repository: IUserRepository = Depends(Stub(IUserRepository)),
        authentication_provider: IAuthenticationAdapter = Depends(Stub(IAuthenticationAdapter)),
        encrypt_adapter: IEncryptionAdapter = Depends(Stub(IEncryptionAdapter))
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
        auth_service: IAuthenticationService = Depends(Stub(IAuthenticationService))
) -> Optional[UserPrivateDTO]:
    return await auth_service.verify_token(token=token)
