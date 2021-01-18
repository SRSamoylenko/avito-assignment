from sqlalchemy import Column, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import relationship

from database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    cost = Column(Float)
    date_added = Column(Date)

    bookings = relationship("Booking", back_populates="room", cascade="all, delete")


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(Integer, primary_key=True, index=True)
    date_start = Column(Date)
    date_end = Column(Date)
    room_id = Column(Integer, ForeignKey("rooms.id"))

    room = relationship("Room", back_populates="bookings")
