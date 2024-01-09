from pydantic import EmailStr
from abc import abstractmethod, ABC

from app.dto.auth import UserPublicDTO, TokenDTO, UserPrivateDTO


class IAuthenticationService(ABC):
    @abstractmethod
    async def register_new_user(self, email: EmailStr, password: str) -> UserPrivateDTO:
        pass

    @abstractmethod
    async def authenticate_user(self, email: EmailStr, password: str) -> UserPublicDTO:
        pass

    @abstractmethod
    async def login_user(self, email: EmailStr, password: str) -> TokenDTO:
        pass

    @abstractmethod
    async def verify_token(self, token: str) -> UserPrivateDTO:
        pass
