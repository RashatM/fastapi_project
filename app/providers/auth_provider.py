from datetime import datetime, timedelta
from jose import jwt

from app.config import settings


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
            data={"sub": user_id}
        )


