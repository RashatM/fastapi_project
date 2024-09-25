from typing import Optional
from pydantic import EmailStr
from sqlalchemy import select

from app.repositories.base import BaseRepository
from app.models.users import UserModel


class UserRepository(BaseRepository):

    async def get_user_by_email(self, email: EmailStr) -> Optional[UserModel]:
        query = select(UserModel.__table__.columns).filter(UserModel.email == email)
        result = await self._session.execute(query)
        return result.one_or_none()

    async def add_new_user(self, email: EmailStr, hashed_password: str) -> UserModel:
        new_user = UserModel(
            email=email,
            hashed_password=hashed_password
        )
        self._session.add(new_user)
        return new_user
