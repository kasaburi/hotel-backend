from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class RoomTypeImage(Base):
    __tablename__ = "room_type_images"

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
            "room_types.id",
            ondelete="CASCADE"
        ),
        nullable=False
    )

    source = Column(
        Text,
        nullable=False
    )

    room_type = relationship(
        "RoomType",
        back_populates="images"
    )