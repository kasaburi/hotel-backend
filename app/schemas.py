from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel, EmailStr, ConfigDict


# =========================================================
# USER / AUTH
# =========================================================

class UserBase(BaseModel):
    firstName: str
    lastName: str
    age: Optional[int] = None
    email: EmailStr
    address: Optional[str] = None
    phone: Optional[str] = None
    zipcode: Optional[str] = None
    avatar: Optional[str] = None
    gender: Optional[str] = None


class UserCreate(UserBase):
    password: str


class UserLogin(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    firstName: str
    lastName: str
    age: Optional[int] = None
    email: EmailStr
    address: Optional[str] = None
    phone: Optional[str] = None
    zipcode: Optional[str] = None
    avatar: Optional[str] = None
    gender: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class TokenResponse(BaseModel):
    token: str
    userId: int
    userEmail: EmailStr


# =========================================================
# ROOM IMAGE
# =========================================================

class RoomImageBase(BaseModel):
    source: str


class RoomImageCreate(RoomImageBase):
    pass


class RoomImageResponse(RoomImageBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# ROOM TYPE
# =========================================================

class RoomTypeBase(BaseModel):
    name_ka: str
    name_en: Optional[str] = None


class RoomTypeCreate(RoomTypeBase):
    pass


class RoomTypeResponse(RoomTypeBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# ROOM
# =========================================================

class RoomBase(BaseModel):
    hotel_id: int
    room_type_id: Optional[int] = None

    name_ka: str
    name_en: Optional[str] = None

    description_ka: Optional[str] = None
    description_en: Optional[str] = None

    price_per_night: float
    max_guests: int = 1
    reservation_count: int = 0


class RoomCreate(RoomBase):
    images: list[RoomImageCreate] = []


class RoomResponse(BaseModel):
    id: int

    hotelId: int
    roomTypeId: Optional[int] = None

    name: str
    roomTypeName: Optional[str] = None

    description: Optional[str] = None

    pricePerNight: float
    maxGuests: int
    reservationCount: int

    images: list[RoomImageResponse] = []

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# HOTEL
# =========================================================

class HotelBase(BaseModel):
    name_ka: str
    name_en: Optional[str] = None

    description_ka: Optional[str] = None
    description_en: Optional[str] = None

    city: str
    featured_image: Optional[str] = None


class HotelCreate(HotelBase):
    pass


class HotelResponse(BaseModel):
    id: int

    name: str
    description: Optional[str] = None

    city: str
    featuredImage: Optional[str] = None

    rooms: list[RoomResponse] = []

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# BOOKING
# =========================================================

class BookingCreate(BaseModel):
    """
    ახალი ჯავშნის შექმნა.

    userId frontend-იდან არ მოდის.
    Backend იღებს მომხმარებლის ID-ს JWT token-იდან.
    """

    roomId: int
    customerName: str

    checkInDate: date
    checkOutDate: date

    guests: int


class BookingResponse(BaseModel):
    id: int

    userId: int
    roomId: int

    customerName: str

    checkInDate: date
    checkOutDate: date

    guests: int

    totalPrice: float

    isConfirmed: bool

    status: str


# =========================================================
# PAYMENT
# =========================================================

class FakePaymentCreate(BaseModel):
    booking_id: int
    amount: float
    payment_method: str = "fake_card"


class FakePaymentResponse(BaseModel):
    id: int
    booking_id: int
    amount: float
    payment_method: str
    status: str

    model_config = ConfigDict(from_attributes=True)


# =========================================================
# REVIEW
# =========================================================

class ReviewCreate(BaseModel):
    hotelId: int
    rating: int
    comment: Optional[str] = None


class ReviewResponse(BaseModel):
    id: int
    userId: int
    hotelId: int
    rating: int
    comment: Optional[str] = None
    createdAt: datetime

    model_config = ConfigDict(from_attributes=True)