from pydantic import BaseModel, EmailStr


class BaseUserSchema(BaseModel):
    email: EmailStr


class UserRequestSchema(BaseUserSchema):
    password: str


class UserPublicSchema(BaseUserSchema):
    id: int
    hashed_password: str


class UserPrivateSchema(BaseUserSchema):
    id: int


class Token(BaseModel):
    access_token: str
