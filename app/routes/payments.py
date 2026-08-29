
from uuid import uuid4

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user_id
from app.models import Booking, Payment
from app.schemas import FakePaymentCreate


router = APIRouter(
    prefix="/api/payments",
    tags=["Payments"]
)


# =========================================================
# FAKE PAYMENT
# =========================================================

@router.post("/fake")
def fake_payment(
    payment_data: FakePaymentCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):

    # -----------------------------------------
    # Booking-ის მოძებნა
    # -----------------------------------------

    booking = (
        db.query(Booking)
        .filter(
            Booking.id == payment_data.bookingId,
            Booking.user_id == user_id
        )
        .first()
    )

    if not booking:
        raise HTTPException(
            status_code=404,
            detail="Booking not found"
        )

    # -----------------------------------------
    # უკვე გადახდილია?
    # -----------------------------------------

    existing_payment = (
        db.query(Payment)
        .filter(
            Payment.booking_id == booking.id
        )
        .first()
    )

    if existing_payment:
        raise HTTPException(
            status_code=400,
            detail="This booking has already been paid"
        )

    # -----------------------------------------
    # მარტივი Fake Card validation
    # -----------------------------------------

    card_number = (
        payment_data.cardNumber
        .replace(" ", "")
        .replace("-", "")
    )

    if len(card_number) != 16 or not card_number.isdigit():
        raise HTTPException(
            status_code=400,
            detail="Invalid card number"
        )

    if len(payment_data.cvv) != 3 or not payment_data.cvv.isdigit():
        raise HTTPException(
            status_code=400,
            detail="Invalid CVV"
        )

    # -----------------------------------------
    # Fake Transaction ID
    # -----------------------------------------

    transaction_id = f"FAKE-{uuid4().hex[:10].upper()}"

    # -----------------------------------------
    # Payment-ის შექმნა
    # -----------------------------------------

    payment = Payment(
        booking_id=booking.id,
        amount=booking.total_price,
        status="paid",
        payment_method="fake_card",
        transaction_id=transaction_id
    )

    db.add(payment)

    # -----------------------------------------
    # Booking-ის დადასტურება
    # -----------------------------------------

    booking.status = "confirmed"
    booking.is_confirmed = True

    db.commit()
    db.refresh(payment)

    return {
        "message": "Payment successful",
        "payment": {
            "id": payment.id,
            "bookingId": payment.booking_id,
            "amount": payment.amount,
            "status": payment.status,
            "paymentMethod": payment.payment_method,
            "transactionId": payment.transaction_id
        },
        "booking": {
            "id": booking.id,
            "status": booking.status,
            "isConfirmed": booking.is_confirmed
        }
    }


# =========================================================
# PAYMENT INFORMATION
# =========================================================

@router.get("/{booking_id}")
def get_payment(
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

    payment = (
        db.query(Payment)
        .filter(
            Payment.booking_id == booking_id
        )
        .first()
    )

    if not payment:
        raise HTTPException(
            status_code=404,
            detail="Payment not found"
        )

    return {
        "id": payment.id,
        "bookingId": payment.booking_id,
        "amount": payment.amount,
        "status": payment.status,
        "paymentMethod": payment.payment_method,
        "transactionId": payment.transaction_id,
        "createdAt": payment.created_at
    }

