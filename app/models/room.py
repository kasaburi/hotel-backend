
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Room, RoomType


router = APIRouter(
    prefix="/api/Rooms",
    tags=["Rooms"]
)


# =========================================================
# GET ALL ROOMS
# =========================================================

@router.get("/GetAll")
def get_all_rooms(db: Session = Depends(get_db)):

    rooms = db.query(Room).all()

    return [
        {
            "id": room.id,

            "name": room.name_en or room.name_ka,

            "description": (
                room.description_en
                or room.description_ka
            ),

            "pricePerNight": float(room.price_per_night),

            "maxGuests": room.max_guests,

            "hotelId": room.hotel_id,

            "roomTypeId": room.room_type_id,

            "roomTypeName": (
                room.room_type.name_en
                or room.room_type.name_ka
                if room.room_type
                else None
            ),

            "reservationCount": room.reservation_count,

            # =================================================
            # ROOM TYPE IMAGES
            # ერთი ტიპის ყველა ოთახი იყენებს ერთსა და იმავე ფოტოებს
            # =================================================

            "images": [
                {
                    "source": image.source
                }
                for image in room.room_type.images
            ] if room.room_type else []
        }

        for room in rooms
    ]


# =========================================================
# GET ROOM TYPES
# =========================================================

@router.get("/GetRoomTypes")
def get_room_types(db: Session = Depends(get_db)):

    room_types = db.query(RoomType).all()

    return [
        {
            "id": room_type.id,

            "name": (
                room_type.name_en
                or room_type.name_ka
            )
        }

        for room_type in room_types
    ]


# =========================================================
# GET SINGLE ROOM
# =========================================================

@router.get("/{room_id}")
def get_room(
    room_id: int,
    db: Session = Depends(get_db)
):

    room = (
        db.query(Room)
        .filter(Room.id == room_id)
        .first()
    )

    if not room:
        raise HTTPException(
            status_code=404,
            detail="Room not found"
        )

    return {
        "id": room.id,

        "name": (
            room.name_en
            or room.name_ka
        ),

        "description": (
            room.description_en
            or room.description_ka
        ),

        "pricePerNight": float(room.price_per_night),

        "maxGuests": room.max_guests,

        "hotelId": room.hotel_id,

        "roomTypeId": room.room_type_id,

        "roomTypeName": (
            room.room_type.name_en
            or room.room_type.name_ka
            if room.room_type
            else None
        ),

        "reservationCount": room.reservation_count,

        # =================================================
        # ROOM TYPE IMAGES
        # =================================================

        "images": [
            {
                "source": image.source
            }
            for image in room.room_type.images
        ] if room.room_type else []
    }

