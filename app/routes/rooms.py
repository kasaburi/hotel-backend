from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Room, RoomType


router = APIRouter(
    prefix="/api/Rooms",
    tags=["Rooms"]
)


@router.get("/GetAll")
def get_all_rooms(db: Session = Depends(get_db)):
    rooms = db.query(Room).all()

    return [
        {
            "id": room.id,

            # Frontend-ისთვის სახელი
            "name": room.name_en or room.name_ka,

            "pricePerNight": room.price_per_night,
            "maxGuests": room.max_guests,
            "hotelId": room.hotel_id,

            "roomTypeId": room.room_type_id,

            "roomTypeName": (
                room.room_type.name
                if room.room_type
                else None
            ),

            "reservationCount": room.reservation_count,

            "images": [
                {
                    "source": image.source
                }
                for image in room.images
            ]
        }
        for room in rooms
    ]


@router.get("/GetRoomTypes")
def get_room_types(db: Session = Depends(get_db)):
    room_types = db.query(RoomType).all()

    return [
        {
            "id": room_type.id,
            "name": room_type.name
        }
        for room_type in room_types
    ]


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

        # Frontend იღებს name-ს
        "name": room.name_en or room.name_ka,

        "description": (
            room.description_en
            or room.description_ka
        ),

        "pricePerNight": room.price_per_night,
        "maxGuests": room.max_guests,
        "hotelId": room.hotel_id,

        "roomTypeId": room.room_type_id,

        "roomTypeName": (
            room.room_type.name
            if room.room_type
            else None
        ),

        "reservationCount": room.reservation_count,

        "images": [
            {
                "source": image.source
            }
            for image in room.images
        ]
    }