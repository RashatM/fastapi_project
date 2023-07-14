from pydantic import EmailStr
from fastapi import Response

from app.adapters.encrypt_adapter import EncryptionAdapter
from app.exceptions.auth import UserAlreadyExistsException, UserIsNotAuthorizedException
from app.models.users import UserModel
from app.providers.auth_provider import AuthenticationProvider
from app.repositories.users import UserRepository
from app.schemas.users import UserAuthSchema, Token
from app.unit_of_work.uow import UnitOfWork


class AuthenticationService:

    def __init__(
            self,
            uow: UnitOfWork,
            user_repository: UserRepository,
            auth_provider: AuthenticationProvider,
            encrypt_adapter: EncryptionAdapter
    ):
        self.uow = uow
        self.user_repository = user_repository
        self.auth_provider = auth_provider
        self.encrypt_adapter = encrypt_adapter

    def is_exist_user(self, email: EmailStr):
        return self.user_repository.get_user_by_email(email=email)

    async def add_user(self, user_data: UserAuthSchema) -> UserModel:
        if await self.is_exist_user(user_data.email):
            raise UserAlreadyExistsException

        hashed_password = self.encrypt_adapter.get_password_hash(user_data.password)

        new_user = await self.user_repository.add_new_user(
            email=user_data.email,
            hashed_password=hashed_password
        )
        await self.uow.commit()

        return new_user

    async def authenticate_user(self, email: EmailStr, password: str) -> UserModel:
        user = await self.is_exist_user(email=email)
        if not (user and self.encrypt_adapter.verify_password(password, user.hashed_password)):
            raise UserIsNotAuthorizedException
        return user

    async def login_user(self, email: EmailStr, password: str) -> Token:
        user = await self.authenticate_user(email=email, password=password)
        access_token = self.auth_provider.create_user_token(user.id)

        return Token(access_token=access_token)
