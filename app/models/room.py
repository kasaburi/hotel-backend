
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Text
from sqlalchemy.orm import relationship

from app.database import Base


class Room(Base):
    __tablename__ = "rooms"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    hotel_id = Column(
        Integer,
        ForeignKey("hotels.id", ondelete="CASCADE"),
        nullable=False
    )

    room_type_id = Column(
        Integer,
        ForeignKey("room_types.id"),
        nullable=True
    )

    # =====================================================
    # ქართული
    # =====================================================

    name_ka = Column(
        String(255),
        nullable=False
    )

    description_ka = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # ინგლისური
    # =====================================================

    name_en = Column(
        String(255),
        nullable=True
    )

    description_en = Column(
        Text,
        nullable=True
    )

    # =====================================================
    # ოთახის ფასი
    # =====================================================

    price_per_night = Column(
        Float,
        nullable=False
    )

    # =====================================================
    # მაქსიმალური სტუმრების რაოდენობა
    # =====================================================

    max_guests = Column(
        Integer,
        nullable=False,
        default=1
    )

    # =====================================================
    # ჯავშნების რაოდენობა
    # =====================================================

    reservation_count = Column(
        Integer,
        nullable=False,
        default=0
    )

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    # Hotel → Rooms
    hotel = relationship(
        "Hotel",
        back_populates="rooms"
    )

    # RoomType → Rooms
    room_type = relationship(
        "RoomType",
        back_populates="rooms"
    )

    # Room → Images
    images = relationship(
        "RoomImage",
        back_populates="room",
        cascade="all, delete-orphan"
    )

    # Room → Bookings
    bookings = relationship(
        "Booking",
        back_populates="room"
    )

class RoomImage(Base):
    __tablename__ = "room_images"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    room_id = Column(
        Integer,
        ForeignKey(
            "rooms.id",
            ondelete="CASCADE"
        ),
        nullable=False,
        index=True
    )