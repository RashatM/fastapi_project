from pydantic import BaseModel, EmailStr


class UserAuthRequestSchema(BaseModel):
    email: EmailStr
    password: str


class UserSchema(BaseModel):
    id: int
    email: EmailStr


class Token(BaseModel):
    access_token: str
