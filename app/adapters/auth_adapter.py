from datetime import datetime, timedelta
from typing import Dict

from jose import jwt, JWTError, ExpiredSignatureError

from app.config import settings
from app.exceptions.auth_exceptions import IncorrectTokenFormatException, UserIsNotPresentException, \
    TokenExpiredException
from app.interfaces.auth_adapter import IAuthenticationAdapter


class AuthenticationAdapter(IAuthenticationAdapter):

    @staticmethod
    def create_access_token(data: dict) -> str:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
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
    def decode_token(token: str) -> Dict[str, str]:
        try:
            payload = jwt.decode(
                token=token,
                key=settings.SECRET_KEY,
                algorithms=settings.ALGORITHM
            )
        except ExpiredSignatureError:
            raise TokenExpiredException
        except JWTError:
            raise IncorrectTokenFormatException

        return payload

    @classmethod
    def get_token_sub(cls, token: str) -> int:
        payload = cls.decode_token(token)

        user_id: int = int(payload.get("sub"))
        if not user_id:
            raise UserIsNotPresentException

        return user_id

