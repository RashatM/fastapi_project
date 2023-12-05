from typing import List, Optional

from sqlalchemy import JSON, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.database import Base


class RoomModel(Base):
    __tablename__ = "rooms"

    id: Mapped[int] = mapped_column(primary_key=True)
    hotel_id: Mapped[str] = mapped_column(ForeignKey("hotels.id"))
    name: Mapped[str]
    description: Mapped[Optional[str]]
    price: Mapped[int]
    services: Mapped[List[str]] = mapped_column(JSON, nullable=True)
    quantity: Mapped[int]
    image_id: Mapped[int]

    hotel: Mapped[str] = relationship(back_populates="rooms")
    booking: Mapped[str] = relationship(back_populates="rooms", primaryjoin="BookingModel.room_id == RoomModel.id")

