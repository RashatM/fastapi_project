from typing import Optional
from pydantic import EmailStr
from sqlalchemy import select
from sqlalchemy.orm import load_only

from app.db.converters.auth import convert_db_model_to_user_dto, convert_db_model_to_private_user_dto
from app.db.repositories.base import BaseRepository
from app.db.models.users import UserModel
from app.schemas.auth import UserPublicSchema, UserPrivateSchema


class UserRepository(BaseRepository):

    async def find_user_by_email(self, email: EmailStr) -> Optional[UserPublicSchema]:
        query = select(UserModel.__table__.columns).filter(UserModel.email == email)
        result = await self._session.execute(query)
        user: Optional[UserModel] = result.one_or_none()

        if user:
            return convert_db_model_to_user_dto(user)

    async def find_user_by_id(self, _id: int) -> Optional[UserPrivateSchema]:
        query = (
            select(UserModel)
            .options(load_only(UserModel.id, UserModel.email))
            .filter(UserModel.id == _id)
        )
        result = await self._session.execute(query)
        user: Optional[UserModel] = result.scalar_one_or_none()

        if user:
            return convert_db_model_to_private_user_dto(user)

    async def add_new_user(self, email: EmailStr, hashed_password: str) -> UserPrivateSchema:
        new_user = UserModel(
            email=email,
            hashed_password=hashed_password
        )
        self._session.add(new_user)
        await self._session.flush()

        return convert_db_model_to_private_user_dto(new_user)
