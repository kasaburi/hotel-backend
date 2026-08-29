from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    first_name = Column(
        String(100),
        nullable=False
    )

    last_name = Column(
        String(100),
        nullable=False
    )

    age = Column(
        Integer,
        nullable=True
    )

    email = Column(
        String(255),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    address = Column(
        String(255),
        nullable=True
    )

    phone = Column(
        String(50),
        nullable=True
    )

    zipcode = Column(
        String(20),
        nullable=True
    )

    avatar = Column(
        String(500),
        nullable=True
    )

    gender = Column(
        String(30),
        nullable=True
    )

    # =====================================================
    # RELATIONSHIPS
    # =====================================================

    # მომხმარებლის ყველა ჯავშანი
    bookings = relationship(
        "Booking",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    # მომხმარებლის ყველა შეფასება
    reviews = relationship(
        "Review",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    # მომხმარებლის გადახდები
    payments = relationship(
        "Payment",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    # მომხმარებლის ფავორიტები
    favorites = relationship(
        "Favorite",
        back_populates="user",
        cascade="all, delete-orphan"
    )