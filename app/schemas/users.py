from pydantic import BaseModel, EmailStr


class UserAuthSchema(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str



