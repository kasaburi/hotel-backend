from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class RoomType(Base):
    __tablename__ = "room_types"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name_ka = Column(
        String(100),
        nullable=False
    )

    name_en = Column(
        String(100),
        nullable=False
    )

    rooms = relationship(
        "Room",
        back_populates="room_type"
    )

    images = relationship(
        "RoomTypeImage",
        back_populates="room_type",
        cascade="all, delete-orphan"
    )