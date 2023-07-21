from sqlalchemy import JSON, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, clear_mappers

from app.db.database import Base


class RoomModel(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True)
    hotel_id = Column(ForeignKey("hotels.id"), nullable=False)
    name = Column(String, nullable=False)
    description = Column(String, nullable=True)
    price = Column(Integer, nullable=False)
    services = Column(JSON, nullable=True)
    quantity = Column(Integer,  nullable=False)
    image_id = Column(Integer)

    # hotel = relationship("HotelModel", back_populates="rooms")
    # booking = relationship("BookingModel", "rooms")
