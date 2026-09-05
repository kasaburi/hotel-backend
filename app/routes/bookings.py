from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session, joinedload

from app.dependencies import get_current_user_id
from app.database import get_db
from app.models import Booking, Room
from app.schemas import BookingCreate


router = APIRouter(
    prefix="/api/Booking",
    tags=["Bookings"]
)


# =========================================================
# CREATE BOOKING
# =========================================================

@router.post("")
def create_booking(
    booking_data: BookingCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    # -----------------------------------------------------
    # FIND ROOM
    # -----------------------------------------------------

    room = (
        db.query(Room)
        .filter(Room.id == booking_data.roomId)
        .first()
    )

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    # -----------------------------------------------------
    # DATE VALIDATION
    # -----------------------------------------------------

    if booking_data.checkOutDate <= booking_data.checkInDate:
        raise HTTPException(
            status_code=400,
            detail="Check-out date must be after check-in date"
        )

    # -----------------------------------------------------
    # GUEST VALIDATION
    # -----------------------------------------------------

    if booking_data.guests < 1:
        raise HTTPException(
            status_code=400,
            detail="Guests must be at least 1"
        )

    if booking_data.guests > room.max_guests:
        raise HTTPException(
            status_code=400,
            detail=(
                f"This room allows maximum "
                f"{room.max_guests} guests"
            )
        )

    # -----------------------------------------------------
    # CALCULATE NIGHTS
    # -----------------------------------------------------

    nights = (
        booking_data.checkOutDate -
        booking_data.checkInDate
    ).days

    if nights <= 0:
        raise HTTPException(
            status_code=400,
            detail="Invalid booking dates"
        )

    # -----------------------------------------------------
    # CALCULATE TOTAL PRICE
    # -----------------------------------------------------

    total_price = (
        float(room.price_per_night) *
        nights
    )

    # -----------------------------------------------------
    # CREATE BOOKING
    # -----------------------------------------------------

    booking = Booking(
        user_id=user_id,
        room_id=booking_data.roomId,
        customer_name=booking_data.customerName,
        check_in_date=booking_data.checkInDate,
        check_out_date=booking_data.checkOutDate,

        # IMPORTANT
        guests=booking_data.guests,

        total_price=total_price,
        is_confirmed=False,
        status="pending"
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    # -----------------------------------------------------
    # RESPONSE
    # -----------------------------------------------------

    return {
        "id": booking.id,
        "userId": booking.user_id,
        "roomId": booking.room_id,

        "customerName": booking.customer_name,

        "checkInDate": booking.check_in_date,
        "checkOutDate": booking.check_out_date,

        "guests": booking.guests,

        "nights": nights,

        "pricePerNight": float(
            room.price_per_night
        ),

        "totalPrice": float(
            booking.total_price
        ),

        "isConfirmed": booking.is_confirmed,

        "status": booking.status,

        "message": "Booking created successfully"
    }


# =========================================================
# GET MY BOOKINGS
# =========================================================

@router.get("")
def get_bookings(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    bookings = (
        db.query(Booking)
        .options(
            joinedload(Booking.room)
            .joinedload(Room.hotel)
        )
        .filter(
            Booking.user_id == user_id
        )
        .all()
    )

    result = []

    for booking in bookings:

        room = booking.room
        hotel = room.hotel if room else None

        result.append({
            "id": booking.id,

            "userId": booking.user_id,

            "roomID": booking.room_id,
            "roomId": booking.room_id,

            "roomName": (
                room.name_en
                if room and room.name_en
                else room.name_ka
                if room
                else None
            ),

            "roomNameKa": (
                room.name_ka
                if room
                else None
            ),

            "roomNameEn": (
                room.name_en
                if room
                else None
            ),

            "roomPricePerNight": (
                float(room.price_per_night)
                if room
                else None
            ),

            "maxGuests": (
                room.max_guests
                if room
                else None
            ),

            "customerName": booking.customer_name,

            "checkInDate": booking.check_in_date,

            "checkOutDate": booking.check_out_date,

            "guests": booking.guests,

            "totalPrice": float(
                booking.total_price
            ),

            "isConfirmed": booking.is_confirmed,

            "status": booking.status,

            "hotelId": (
                hotel.id
                if hotel
                else None
            ),

            "hotelName": (
                hotel.name_en
                if hotel and hotel.name_en
                else hotel.name_ka
                if hotel
                else None
            ),

            "hotelNameKa": (
                hotel.name_ka
                if hotel
                else None
            ),

            "hotelNameEn": (
                hotel.name_en
                if hotel
                else None
            ),

            "city": (
                hotel.city
                if hotel
                else None
            ),

            "hotelImage": (
                hotel.featured_image
                if hotel
                else None
            )
        })

    return result


# =========================================================
# GET SINGLE BOOKING
# =========================================================

@router.get("/{booking_id}")
def get_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    booking = (
        db.query(Booking)
        .options(
            joinedload(Booking.room)
            .joinedload(Room.hotel)
        )
        .filter(
            Booking.id == booking_id,
            Booking.user_id == user_id
        )
        .first()
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    room = booking.room
    hotel = room.hotel if room else None

    return {
        "id": booking.id,

        "userId": booking.user_id,

        "roomID": booking.room_id,
        "roomId": booking.room_id,

        "roomName": (
            room.name_en
            if room and room.name_en
            else room.name_ka
            if room
            else None
        ),

        "roomNameKa": (
            room.name_ka
            if room
            else None
        ),

        "roomNameEn": (
            room.name_en
            if room
            else None
        ),

        "roomPricePerNight": (
            float(room.price_per_night)
            if room
            else None
        ),

        "maxGuests": (
            room.max_guests
            if room
            else None
        ),

        "customerName": booking.customer_name,

        "checkInDate": booking.check_in_date,

        "checkOutDate": booking.check_out_date,

        "guests": booking.guests,

        "totalPrice": float(
            booking.total_price
        ),

        "isConfirmed": booking.is_confirmed,

        "status": booking.status,

        "hotelId": (
            hotel.id
            if hotel
            else None
        ),

        "hotelName": (
            hotel.name_en
            if hotel and hotel.name_en
            else hotel.name_ka
            if hotel
            else None
        ),

        "hotelNameKa": (
            hotel.name_ka
            if hotel
            else None
        ),

        "hotelNameEn": (
            hotel.name_en
            if hotel
            else None
        ),

        "city": (
            hotel.city
            if hotel
            else None
        ),

        "hotelImage": (
            hotel.featured_image
            if hotel
            else None
        )
    }


# =========================================================
# CANCEL / DELETE BOOKING
# =========================================================

@router.delete("/{booking_id}")
def delete_booking(
    booking_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):
    booking = (
        db.query(Booking)
        .filter(
            Booking.id == booking_id,
            Booking.user_id == user_id
        )
        .first()
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    db.delete(booking)
    db.commit()

    return {
        "message": "Booking deleted successfully"
    }