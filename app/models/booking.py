from sqlalchemy import (
    Column,
    Integer,
    String,
    Float,
    Boolean,
    Date,
    ForeignKey
)
from sqlalchemy.orm import relationship

from app.database import Base


class Booking(Base):
    __tablename__ = "bookings"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    user_id = Column(
        Integer,
        ForeignKey(
            "users.id",
            ondelete="SET NULL"
        ),
        nullable=True,
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

    customer_name = Column(
        String(255),
        nullable=False
    )

    check_in_date = Column(
        Date,
        nullable=False
    )

    check_out_date = Column(
        Date,
        nullable=False
    )

    total_price = Column(
        Float,
        nullable=False
    )

    is_confirmed = Column(
        Boolean,
        nullable=False,
        default=False
    )

    status = Column(
        String(30),
        nullable=False,
        default="pending"
    )

    user = relationship(
        "User",
        back_populates="bookings"
    )

    room = relationship(
        "Room",
        back_populates="bookings"
    )

    payment = relationship(
        "Payment",
        back_populates="booking",
        uselist=False,
        cascade="all, delete-orphan"
    )