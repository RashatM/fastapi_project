from datetime import datetime, timedelta
from jose import jwt
from passlib.context import CryptContext

from app.config import settings


class AuthProvider:

    def __init__(self):
        self.pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    def get_password_hash(self, password: str) -> str:
        return self.pwd_context.hash(password)

    def verify_password(self, plain_password, hashed_password) -> bool:
        return self.pwd_context.verify(plain_password, hashed_password)

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

    async def authenticate_user(self, email: EmailStr, password: str) -> UserModel:
        user = await self.uow.user_repository.get_user_by_email(email=email)
        if not (user and verify_password(password, user.hashed_password)):
            raise UserIsNotAuthorizedException
        return user

    async def login_user(self, response: Response, email: EmailStr, password: str) -> Token:
        user = await self.authenticate_user(email=email, password=password)
        access_token = create_user_token(user.id)
        response.set_cookie("booking_access_token", access_token, httponly=True)
        return Token(access_token)
