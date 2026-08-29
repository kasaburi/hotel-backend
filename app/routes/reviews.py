from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.dependencies import get_current_user_id
from app.models import Review, Hotel
from app.schemas import ReviewCreate


router = APIRouter(
    prefix="/api/reviews",
    tags=["Reviews"]
)


# =========================================================
# HOTEL REVIEWS
# =========================================================

@router.get("/hotel/{hotel_id}")
def get_hotel_reviews(
    hotel_id: int,
    db: Session = Depends(get_db)
):

    hotel = (
        db.query(Hotel)
        .filter(Hotel.id == hotel_id)
        .first()
    )

    if not hotel:
        raise HTTPException(
            status_code=404,
            detail="Hotel not found"
        )

    reviews = (
        db.query(Review)
        .filter(
            Review.hotel_id == hotel_id
        )
        .order_by(
            Review.created_at.desc()
        )
        .all()
    )

    return [
        {
            "id": review.id,
            "userId": review.user_id,
            "hotelId": review.hotel_id,
            "rating": review.rating,
            "comment": review.comment,
            "createdAt": review.created_at
        }
        for review in reviews
    ]


# =========================================================
# CREATE REVIEW
# =========================================================

@router.post("")
def create_review(
    review_data: ReviewCreate,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):

    hotel = (
        db.query(Hotel)
        .filter(
            Hotel.id == review_data.hotelId
        )
        .first()
    )

    if not hotel:
        raise HTTPException(
            status_code=404,
            detail="Hotel not found"
        )

    # -----------------------------------------
    # Rating validation
    # -----------------------------------------

    if review_data.rating < 1 or review_data.rating > 5:
        raise HTTPException(
            status_code=400,
            detail="Rating must be between 1 and 5"
        )

    # -----------------------------------------
    # მომხმარებელს უკვე აქვს შეფასება?
    # -----------------------------------------

    existing_review = (
        db.query(Review)
        .filter(
            Review.user_id == user_id,
            Review.hotel_id == review_data.hotelId
        )
        .first()
    )

    if existing_review:
        raise HTTPException(
            status_code=400,
            detail="You have already reviewed this hotel"
        )

    # -----------------------------------------
    # Review
    # -----------------------------------------

    review = Review(
        user_id=user_id,
        hotel_id=review_data.hotelId,
        rating=review_data.rating,
        comment=review_data.comment
    )

    db.add(review)
    db.commit()
    db.refresh(review)

    # -----------------------------------------
    # Hotel rating-ის განახლება
    # -----------------------------------------

    reviews = (
        db.query(Review)
        .filter(
            Review.hotel_id == hotel.id
        )
        .all()
    )

    if reviews:
        hotel.rating = sum(
            r.rating for r in reviews
        ) / len(reviews)

    db.commit()

    return {
        "message": "Review added successfully",
        "review": {
            "id": review.id,
            "hotelId": review.hotel_id,
            "rating": review.rating,
            "comment": review.comment
        }
    }


# =========================================================
# DELETE REVIEW
# =========================================================

@router.delete("/{review_id}")
def delete_review(
    review_id: int,
    db: Session = Depends(get_db),
    user_id: int = Depends(get_current_user_id)
):

    review = (
        db.query(Review)
        .filter(
            Review.id == review_id,
            Review.user_id == user_id
        )
        .first()
    )

    if not review:
        raise HTTPException(
            status_code=404,
            detail="Review not found"
        )

    hotel_id = review.hotel_id

    db.delete(review)
    db.commit()

    # -----------------------------------------
    # Rating-ის ხელახლა დათვლა
    # -----------------------------------------

    hotel = (
        db.query(Hotel)
        .filter(Hotel.id == hotel_id)
        .first()
    )

    if hotel:
        reviews = (
            db.query(Review)
            .filter(
                Review.hotel_id == hotel_id
            )
            .all()
        )

        if reviews:
            hotel.rating = sum(
                r.rating for r in reviews
            ) / len(reviews)
        else:
            hotel.rating = 0

        db.commit()

    return {
        "message": "Review deleted successfully"
    }
