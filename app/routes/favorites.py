
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user_id
from app.models import Favorite, Hotel


router = APIRouter(
    prefix="/api/favorites",
    tags=["Favorites"]
)


# =========================================================
# GET USER FAVORITES
# =========================================================

@router.get("")
def get_favorites(
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):

    favorites = (
        db.query(Favorite)
        .filter(
            Favorite.user_id == user_id
        )
        .all()
    )

    result = []

    for favorite in favorites:

        hotel = (
            db.query(Hotel)
            .filter(
                Hotel.id == favorite.hotel_id
            )
            .first()
        )

        if hotel:
            result.append({
                "id": favorite.id,
                "hotelId": hotel.id,
                "name": hotel.name_en or hotel.name_ka,
                "city": hotel.city,
                "featuredImage": hotel.featured_image,
                "rating": hotel.rating
            })

    return result


# =========================================================
# ADD FAVORITE
# =========================================================

@router.post("/{hotel_id}")
def add_favorite(
    hotel_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):

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

    existing = (
        db.query(Favorite)
        .filter(
            Favorite.user_id == user_id,
            Favorite.hotel_id == hotel_id
        )
        .first()
    )

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Hotel is already in favorites"
        )

    favorite = Favorite(
        user_id=user_id,
        hotel_id=hotel_id
    )

    db.add(favorite)
    db.commit()
    db.refresh(favorite)

    return {
        "message": "Hotel added to favorites",
        "favorite": {
            "id": favorite.id,
            "hotelId": favorite.hotel_id
        }
    }


# =========================================================
# REMOVE FAVORITE
# =========================================================

@router.delete("/{hotel_id}")
def remove_favorite(
    hotel_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):

    favorite = (
        db.query(Favorite)
        .filter(
            Favorite.user_id == user_id,
            Favorite.hotel_id == hotel_id
        )
        .first()
    )

    if not favorite:
        raise HTTPException(
            status_code=404,
            detail="Hotel is not in favorites"
        )

    db.delete(favorite)
    db.commit()

    return {
        "message": "Hotel removed from favorites"
    }

