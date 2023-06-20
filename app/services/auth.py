from typing import Optional

from pydantic import EmailStr

from app.auth.auth import get_password_hash, verify_password, create_user_token
from app.exceptions.auth import UserAlreadyExistsException, UserIsNotAuthorizedException
from app.models.users import User
from app.schemas.users import UserAuthSchema
from app.services.base import BaseService


class UserService(BaseService):

    async def add_user(self, user_data: UserAuthSchema) -> None:
        exist_user = await self.uow.user_repository.get_user_by_email(email=user_data.email)
        if exist_user:
            raise UserAlreadyExistsException

        hashed_password = get_password_hash(user_data.password)

        await self.uow.user_repository.add_new_user(email=user_data.email, hashed_password=hashed_password)
        await self.uow.commit()

    async def authenticate_user(self, email: EmailStr, password: str) -> User:
        user = await self.uow.user_repository.get_user_by_email(email=email)
        if not user or not verify_password(password, user.hashed_password):
            raise UserIsNotAuthorizedException
        return user

    async def login_user(self, email: EmailStr, password: str):
        user = await self.authenticate_user(email=email, password=password)
        access_token = create_user_token(user.id)





