from datetime import date

from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Hotel, Room, RoomType


router = APIRouter(
    prefix="/api/hotels",
    tags=["Hotels"]
)


# =========================================================
# GET HOTELS + FILTERS
# =========================================================

@router.get("")
def get_hotels(
    city: str | None = Query(default=None),

    check_in: date | None = Query(default=None),

    check_out: date | None = Query(default=None),

    guests: int | None = Query(
        default=None,
        ge=1
    ),

    min_price: float | None = Query(
        default=None,
        ge=0
    ),

    max_price: float | None = Query(
        default=None,
        ge=0
    ),

    room_type_id: int | None = Query(
        default=None
    ),

    rating: float | None = Query(
        default=None,
        ge=0,
        le=5
    ),

    sort: str | None = Query(default=None),

    db: Session = Depends(get_db)
):

    # =====================================================
    # DATE VALIDATION
    # =====================================================

    if check_in and check_out:

        if check_out <= check_in:
            raise HTTPException(
                status_code=400,
                detail="Check-out date must be after check-in date"
            )

    # =====================================================
    # PRICE VALIDATION
    # =====================================================

    if min_price is not None and max_price is not None:

        if min_price > max_price:
            raise HTTPException(
                status_code=400,
                detail="Minimum price cannot be greater than maximum price"
            )

    # =====================================================
    # BASE HOTEL QUERY
    # =====================================================

    query = db.query(Hotel)

    # =====================================================
    # CITY FILTER
    # =====================================================

    if city:

        query = query.filter(
            Hotel.city.ilike(f"%{city}%")
        )

    # =====================================================
    # RATING FILTER
    # =====================================================

    if rating is not None:

        query = query.filter(
            Hotel.rating >= rating
        )

    hotels = query.all()

    result = []

    # =====================================================
    # PROCESS HOTELS
    # =====================================================

    for hotel in hotels:

        # =================================================
        # ROOMS QUERY
        # =================================================

        rooms_query = (
            db.query(Room)
            .filter(
                Room.hotel_id == hotel.id
            )
        )

        # =================================================
        # GUESTS FILTER
        # =================================================

        if guests is not None:

            rooms_query = rooms_query.filter(
                Room.max_guests >= guests
            )

        # =================================================
        # ROOM TYPE FILTER
        # =================================================

        if room_type_id is not None:

            rooms_query = rooms_query.filter(
                Room.room_type_id == room_type_id
            )

        rooms = rooms_query.all()

        # =================================================
        # PRICE FILTER
        # =================================================

        if min_price is not None:

            rooms = [
                room
                for room in rooms
                if float(room.price_per_night) >= min_price
            ]

        if max_price is not None:

            rooms = [
                room
                for room in rooms
                if float(room.price_per_night) <= max_price
            ]

        # =================================================
        # AVAILABILITY FILTER
        # =================================================

        if check_in and check_out:

            available_rooms = []

            for room in rooms:

                overlapping_booking = any(
                    booking.check_in_date < check_out
                    and booking.check_out_date > check_in
                    and booking.status != "cancelled"
                    for booking in room.bookings
                )

                if not overlapping_booking:
                    available_rooms.append(room)

            rooms = available_rooms

        # =================================================
        # IF NO ROOMS MATCH
        # =================================================

        if not rooms:
            continue

        # =================================================
        # HOTEL IMAGES
        # =================================================

        hotel_images = [
            {
                "id": image.id,
                "source": image.source
            }
            for image in hotel.images
        ]

        # =================================================
        # ROOMS RESPONSE
        # =================================================

        rooms_result = []

        for room in rooms:

            # ---------------------------------------------
            # ROOM TYPE
            # ---------------------------------------------

            room_type = room.room_type

            room_type_name = None

            if room_type:

                room_type_name = (
                    room_type.name_en
                    or room_type.name_ka
                )

            # ---------------------------------------------
            # ROOM IMAGES
            # ---------------------------------------------

            room_images = [
                {
                    "id": image.id,
                    "source": image.source
                }
                for image in room.images
            ]

            # ---------------------------------------------
            # ROOM TYPE IMAGES
            # ---------------------------------------------

            room_type_images = []

            if room_type:

                room_type_images = [
                    {
                        "id": image.id,
                        "source": image.source
                    }
                    for image in room_type.images
                ]

            # ---------------------------------------------
            # ROOM
            # ---------------------------------------------

            rooms_result.append({

                "id": room.id,

                "name": (
                    room.name_en
                    or room.name_ka
                ),

                "description": (
                    room.description_en
                    or room.description_ka
                ),

                "pricePerNight": float(
                    room.price_per_night
                ),

                "maxGuests": room.max_guests,

                "reservationCount": room.reservation_count,

                "roomTypeId": room.room_type_id,

                "roomTypeName": room_type_name,

                "images": room_images,

                "roomTypeImages": room_type_images
            })

        # =================================================
        # HOTEL RESPONSE
        # =================================================

        result.append({

            "id": hotel.id,

            "name": (
                hotel.name_en
                or hotel.name_ka
            ),

            "description": (
                hotel.description_en
                or hotel.description_ka
            ),

            "city": hotel.city,

            "featuredImage": hotel.featured_image,

            "rating": hotel.rating,

            "images": hotel_images,

            "rooms": rooms_result
        })

    # =====================================================
    # SORTING
    # =====================================================

    if sort == "price_asc":

        result.sort(
            key=lambda hotel: min(
                room["pricePerNight"]
                for room in hotel["rooms"]
            )
        )

    elif sort == "price_desc":

        result.sort(
            key=lambda hotel: max(
                room["pricePerNight"]
                for room in hotel["rooms"]
            ),
            reverse=True
        )

    elif sort == "rating_desc":

        result.sort(
            key=lambda hotel: hotel["rating"] or 0,
            reverse=True
        )

    elif sort == "rating_asc":

        result.sort(
            key=lambda hotel: hotel["rating"] or 0
        )

    return result


# =========================================================
# GET ONE HOTEL
# =========================================================

@router.get("/{hotel_id}")
def get_hotel(
    hotel_id: int,
    db: Session = Depends(get_db)
):

    # =====================================================
    # FIND HOTEL
    # =====================================================

    hotel = (
        db.query(Hotel)
        .filter(
            Hotel.id == hotel_id
        )
        .first()
    )

    if not hotel:

        raise HTTPException(
            status_code=404,
            detail="Hotel not found"
        )

    # =====================================================
    # HOTEL IMAGES
    # =====================================================

    hotel_images = [
        {
            "id": image.id,
            "source": image.source
        }
        for image in hotel.images
    ]

    # =====================================================
    # ROOMS
    # =====================================================

    rooms_result = []

    for room in hotel.rooms:

        # -------------------------------------------------
        # ROOM TYPE
        # -------------------------------------------------

        room_type = room.room_type

        room_type_name = None

        if room_type:

            room_type_name = (
                room_type.name_en
                or room_type.name_ka
            )

        # -------------------------------------------------
        # ROOM IMAGES
        # -------------------------------------------------

        room_images = [
            {
                "id": image.id,
                "source": image.source
            }
            for image in room.images
        ]

        # -------------------------------------------------
        # ROOM TYPE IMAGES
        # -------------------------------------------------

        room_type_images = []

        if room_type:

            room_type_images = [
                {
                    "id": image.id,
                    "source": image.source
                }
                for image in room_type.images
            ]

        # -------------------------------------------------
        # ROOM RESPONSE
        # -------------------------------------------------

        rooms_result.append({

            "id": room.id,

            "name": (
                room.name_en
                or room.name_ka
            ),

            "description": (
                room.description_en
                or room.description_ka
            ),

            "pricePerNight": float(
                room.price_per_night
            ),

            "maxGuests": room.max_guests,

            "reservationCount": room.reservation_count,

            "roomTypeId": room.room_type_id,

            "roomTypeName": room_type_name,

            "images": room_images,

            "roomTypeImages": room_type_images
        })

    # =====================================================
    # FINAL HOTEL RESPONSE
    # =====================================================

    return {

        "id": hotel.id,

        "name": (
            hotel.name_en
            or hotel.name_ka
        ),

        "description": (
            hotel.description_en
            or hotel.description_ka
        ),

        "city": hotel.city,

        "featuredImage": hotel.featured_image,

        "rating": hotel.rating,

        "images": hotel_images,

        "rooms": rooms_result
    }