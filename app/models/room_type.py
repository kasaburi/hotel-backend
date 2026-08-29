from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class RoomType(Base):
    __tablename__ = "room_types"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False, unique=True)

    rooms = relationship("Room", back_populates="room_type")