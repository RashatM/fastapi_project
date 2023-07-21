from sqlalchemy import JSON, Column, Integer, String
from sqlalchemy.orm import relationship

from app.db.database import Base


class HotelModel(Base):
    __tablename__ = "hotels"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    location = Column(String, nullable=False)
    services = Column(JSON)
    rooms_quantity = Column(Integer, nullable=False)
    image_id = Column(Integer)

    # rooms = relationship("RoomModel", back_populates="hotel")
