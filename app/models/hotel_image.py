from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base


class HotelImage(Base):
    __tablename__ = "hotel_images"

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
        nullable=False,
        index=True
    )

    source = Column(
        String(500),
        nullable=False
    )

    hotel = relationship(
        "Hotel",
        back_populates="images"
    )