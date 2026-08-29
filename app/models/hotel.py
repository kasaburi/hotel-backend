

from sqlalchemy import Column, Integer, String, Text, Float
from sqlalchemy.orm import relationship

from app.database import Base


class Hotel(Base):
    __tablename__ = "hotels"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name_ka = Column(
        String(255),
        nullable=False
    )

    description_ka = Column(
        Text,
        nullable=True
    )

    name_en = Column(
        String(255),
        nullable=True
    )

    description_en = Column(
        Text,
        nullable=True
    )

    city = Column(
        String(100),
        nullable=False,
        index=True
    )

    featured_image = Column(
        String(500),
        nullable=True
    )

    rating = Column(
        Float,
        nullable=False,
        default=0
    )

    rooms = relationship(
        "Room",
        back_populates="hotel",
        cascade="all, delete-orphan"
    )

    images = relationship(
        "HotelImage",
        back_populates="hotel",
        cascade="all, delete-orphan"
    )

    reviews = relationship(
        "Review",
        back_populates="hotel",
        cascade="all, delete-orphan"
    )

    favorites = relationship(
        "Favorite",
        back_populates="hotel",
        cascade="all, delete-orphan"
    )