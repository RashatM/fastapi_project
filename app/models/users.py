from sqlalchemy import Column, String, Integer

from app.database import Base
from app.schemas.auth import UserSchema


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    def to_dc(self) -> UserSchema:
        return UserSchema(
            id=self.id,
            email=self.email
        )



