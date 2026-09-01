from sqlalchemy import Column, Integer, Text, ForeignKey, Numeric, String
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
        ForeignKey(
            "hotels.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    room_type_id = Column(
        Integer,
        ForeignKey(
            "room_types.id"
        ),
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
    # ფასი
    # =====================================================

    price_per_night = Column(
        Numeric(10, 2),
        nullable=False
    )

    # =====================================================
    # მაქსიმალური სტუმრები
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

    hotel = relationship(
        "Hotel",
        back_populates="rooms"
    )

    room_type = relationship(
        "RoomType",
        back_populates="rooms"
    )

    images = relationship(
        "RoomImage",
        back_populates="room",
        cascade="all, delete-orphan"
    )

    bookings = relationship(
        "Booking",
        back_populates="room"
    )