from typing import List

from sqlalchemy import String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String, nullable=False)
    hashed_password: Mapped[str] = mapped_column(nullable=False)

    booking: Mapped[List["BookingModel"]] = relationship(back_populates="user")



