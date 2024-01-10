from pydantic import EmailStr

from app.exceptions.auth_exceptions import UserAlreadyExistsException, UserIsNotAuthorizedException, \
    UserIsNotExistsException
from app.interfaces.adapters.encrypt_adapter import IEncryptionAdapter
from app.interfaces.auth_adapter import IAuthenticationAdapter
from app.interfaces.repositories.users import IUserRepository
from app.interfaces.services.auth import IAuthenticationService
from app.dto.auth import UserPublicDTO, TokenDTO, UserPrivateDTO
from app.interfaces.uow import IUnitOfWork


class AuthenticationService(IAuthenticationService):

    def __init__(
        self,
        uow: IUnitOfWork,
        user_repository: IUserRepository,
        auth_adapter: IAuthenticationAdapter,
        encrypt_adapter: IEncryptionAdapter
    ):
        self.uow = uow
        self.user_repository = user_repository
        self.auth_adapter = auth_adapter
        self.encrypt_adapter = encrypt_adapter

    async def register_new_user(self, email: EmailStr, password: str) -> UserPrivateDTO:
        if await self.user_repository.find_user_by_email(email):
            raise UserAlreadyExistsException

        hashed_password = self.encrypt_adapter.get_password_hash(password)

        new_user = await self.user_repository.add_new_user(
            email=email,
            hashed_password=hashed_password
        )
        await self.uow.commit()
        return new_user

    async def authenticate_user(self, email: EmailStr, password: str) -> UserPublicDTO:
        user = await self.user_repository.find_user_by_email(email=email)
        if not (user and self.encrypt_adapter.verify_password(password, user.hashed_password)):
            raise UserIsNotAuthorizedException
        return user

    async def login_user(self, email: EmailStr, password: str) -> TokenDTO:
        user = await self.authenticate_user(email=email, password=password)
        access_token = self.auth_adapter.create_user_token(user.id)

        return TokenDTO(access_token=access_token)

    async def verify_token(self, token: str) -> UserPrivateDTO:
        user_id = self.auth_adapter.get_token_sub(token)
        user = await self.user_repository.find_user_by_id(user_id)
        if not user:
            raise UserIsNotExistsException
        return user
