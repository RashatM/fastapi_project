from pydantic import EmailStr

from app.adapters.encrypt_adapter import EncryptionAdapter
from app.exceptions.auth_exceptions import UserAlreadyExistsException, UserIsNotAuthorizedException, \
    UserIsNotExistsException
from app.providers.auth_provider import AuthenticationProvider
from app.db.repositories.users import UserRepository
from app.schemas.auth import UserPublicSchema, Token, UserPrivateSchema
from app.db.unit_of_work.uow import UnitOfWork


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

    async def register_new_user(self, email: EmailStr, password: str) -> UserPrivateSchema:
        if await self.user_repository.find_user_by_email(email):
            raise UserAlreadyExistsException

        hashed_password = self.encrypt_adapter.get_password_hash(password)

        new_user = await self.user_repository.add_new_user(
            email=email,
            hashed_password=hashed_password
        )
        await self.uow.commit()
        return new_user

    async def authenticate_user(self, email: EmailStr, password: str) -> UserPublicSchema:
        user = await self.user_repository.find_user_by_email(email=email)
        if not (user and self.encrypt_adapter.verify_password(password, user.hashed_password)):
            raise UserIsNotAuthorizedException
        return user

    async def login_user(self, email: EmailStr, password: str) -> Token:
        user = await self.authenticate_user(email=email, password=password)
        access_token = self.auth_provider.create_user_token(user.id)

        return Token(access_token=access_token)

    async def verify_token(self, token: str) -> UserPrivateSchema:
        user_id = self.auth_provider.get_token_sub(token)
        user = await self.user_repository.find_user_by_id(user_id)
        if not user:
            raise UserIsNotExistsException
        return user
