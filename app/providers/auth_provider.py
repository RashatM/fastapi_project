from datetime import datetime, timedelta
from jose import jwt, JWTError

from app.config import settings
from app.exceptions.auth_exceptions import IncorrectTokenFormatException, UserIsNotPresentException


class AuthenticationProvider:

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

    @classmethod
    def create_user_token(cls, user_id: int) -> str:
        return cls.create_access_token(
            data={"sub": str(user_id)}
        )

    @staticmethod
    def decode_token(token):
        try:
            payload = jwt.decode(
                token=token,
                key=settings.SECRET_KEY,
                algorithms=settings.ALGORITHM
            )
        except JWTError:
            raise IncorrectTokenFormatException

        user_id: int = int(payload.get("sub"))
        if not user_id:
            raise UserIsNotPresentException

        return user_id


