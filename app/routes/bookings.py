
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

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
    # ვამოწმებთ არსებობს თუ არა ოთახი
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

    # ვამოწმებთ თარიღებს
    if booking_data.checkOutDate <= booking_data.checkInDate:
        raise HTTPException(
            status_code=400,
            detail="Check-out date must be after check-in date"
        )

    # ვქმნით ახალ ჯავშანს
    booking = Booking(
        user_id=user_id,
        room_id=booking_data.roomId,
        customer_name=booking_data.customerName,
        check_in_date=booking_data.checkInDate,
        check_out_date=booking_data.checkOutDate,
        total_price=booking_data.totalPrice,
        is_confirmed=booking_data.isConfirmed
    )

    db.add(booking)
    db.commit()
    db.refresh(booking)

    return {
        "id": booking.id,
        "userId": booking.user_id,
        "roomId": booking.room_id,
        "customerName": booking.customer_name,
        "checkInDate": booking.check_in_date,
        "checkOutDate": booking.check_out_date,
        "totalPrice": booking.total_price,
        "isConfirmed": booking.is_confirmed,
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
        .filter(Booking.user_id == user_id)
        .all()
    )

    result = []

    for booking in bookings:

        room = (
            db.query(Room)
            .filter(Room.id == booking.room_id)
            .first()
        )

        result.append({
            "id": booking.id,
            "userId": booking.user_id,
            "roomID": booking.room_id,
            "customerName": booking.customer_name,
            "checkInDate": booking.check_in_date,
            "checkOutDate": booking.check_out_date,
            "totalPrice": booking.total_price,
            "isConfirmed": booking.is_confirmed,
            "hotelId": room.hotel_id if room else None
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

    room = (
        db.query(Room)
        .filter(Room.id == booking.room_id)
        .first()
    )

    return {
        "id": booking.id,
        "userId": booking.user_id,
        "roomID": booking.room_id,
        "customerName": booking.customer_name,
        "checkInDate": booking.check_in_date,
        "checkOutDate": booking.check_out_date,
        "totalPrice": booking.total_price,
        "isConfirmed": booking.is_confirmed,
        "hotelId": room.hotel_id if room else None
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

