from abc import abstractmethod, ABC
from typing import Optional
from pydantic import EmailStr


from app.dto.auth import UserPublicDTO, UserPrivateDTO


class IUserRepository(ABC):
    @abstractmethod
    async def find_user_by_email(self, email: EmailStr) -> Optional[UserPublicDTO]:
        pass

    @abstractmethod
    async def find_user_by_id(self, _id: int) -> Optional[UserPrivateDTO]:
        pass

    @abstractmethod
    async def add_new_user(self, email: EmailStr, hashed_password: str) -> UserPrivateDTO:
        pass
