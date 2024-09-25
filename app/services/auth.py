from passlib.hash import bcrypt
from pydantic import EmailStr
from fastapi import Response
from datetime import datetime, timedelta
from jose import jwt


from app.auth.auth import get_password_hash, verify_password, create_user_token
from app.exceptions.auth import UserAlreadyExistsException, UserIsNotAuthorizedException
from app.models.users import UserModel
from app.schemas.users import UserAuthSchema, Token
from app.services.base import BaseService
from app.config import settings


class AuthService(BaseService):

    @staticmethod
    def get_password_hash(password: str) -> str:
        return bcrypt.hash(password)

    @staticmethod
    def verify_password(plain_password, hashed_password) -> bool:
        return bcrypt.verify(plain_password, hashed_password)

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=30)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(
            claims=to_encode,
            key=settings.SECRET_KEY,
            algorithm=settings.ALGORITHM
        )
        return encoded_jwt

    def create_user_token(self, user_id: int) -> str:
        return self.create_access_token(
            data={"sub": user_id}
        )

    async def add_user(self, user_data: UserAuthSchema) -> UserModel:
        exist_user = await self.uow.user_repository.get_user_by_email(email=user_data.email)
        if exist_user:
            raise UserAlreadyExistsException

        hashed_password = get_password_hash(user_data.password)

        new_user = await self.uow.user_repository.add_new_user(
            email=user_data.email,
            hashed_password=hashed_password
        )
        await self.uow.commit()

        return new_user

    async def authenticate_user(self, email: EmailStr, password: str) -> UserModel:
        user = await self.uow.user_repository.get_user_by_email(email=email)
        if not (user and verify_password(password, user.hashed_password)):
            raise UserIsNotAuthorizedException
        return user

    async def login_user(self, response: Response, email: EmailStr, password: str) -> Token:
        user = await self.authenticate_user(email=email, password=password)
        access_token = create_user_token(user.id)
        response.set_cookie("booking_access_token", access_token, httponly=True)

        return Token(access_token=access_token)
