from fastapi import Depends
from pydantic import EmailStr
from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.base import BaseRepository
from app.models.users import User


class UserRepository(BaseRepository):

    def __init__(self, session: AsyncSession):
        super().__init__(model=User, session=session)

    async def get_user_by_email(self, email: EmailStr) -> User:
        user = await self.find_one_or_none(email=email)
        return user

    async def add_new_user(self, email: EmailStr, hashed_password: str) -> None:
        await self.add(email=email, hashed_password=hashed_password)



