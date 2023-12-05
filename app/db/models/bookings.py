from datetime import date
from sqlalchemy import Computed, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.database import Base


class BookingModel(Base):
    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    date_from: Mapped[date]
    date_to: Mapped[date]
    price: Mapped[int]
    total_cost: Mapped[int] = mapped_column(Computed("(date_to - date_from) * price"))
    total_days: Mapped[int] = mapped_column(Computed("date_to - date_from"))

    user: Mapped["UserModel"] = relationship(back_populates="booking")
    rooms: Mapped["RoomModel"] = relationship(back_populates="booking", primaryjoin="BookingModel.room_id == RoomModel.id")