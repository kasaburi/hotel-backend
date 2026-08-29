from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


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

    source = Column(
        String(500),
        nullable=False
    )

    room = relationship(
        "Room",
        back_populates="images"
    )