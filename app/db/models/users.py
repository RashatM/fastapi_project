from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.db.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)

    booking = relationship("BookingModel", back_populates="user")



