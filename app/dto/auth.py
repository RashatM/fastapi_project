from pydantic import BaseModel, EmailStr


class BaseUserDTO(BaseModel):
    email: EmailStr


class UserPublicDTO(BaseUserDTO):
    id: int
    hashed_password: str


class UserPrivateDTO(BaseUserDTO):
    id: int


class TokenDTO(BaseModel):
    access_token: str
