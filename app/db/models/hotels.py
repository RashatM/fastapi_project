from typing import List

from sqlalchemy import JSON
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.database import Base


class HotelModel(Base):
    __tablename__ = "hotels"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    location: Mapped[str]
    services: Mapped[List[str]] = mapped_column(JSON)
    rooms_quantity: Mapped[int]
    image_id: Mapped[int]

    rooms: Mapped[List["RoomModel"]] = relationship(back_populates="hotel")
