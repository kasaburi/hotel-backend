from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.middleware.gzip import GZipMiddleware

# =========================================================
# MODELS
# =========================================================

from app.models import (
    User,
    Hotel,
    HotelImage,
    Room,
    RoomImage,
    RoomType,
    RoomTypeImage,
    Booking,
    Payment,
    Review,
    Favorite
)

# =========================================================
# ROUTERS
# =========================================================

from app.routes.auth import router as auth_router
from app.routes.hotels import router as hotels_router
from app.routes.rooms import router as rooms_router
from app.routes.bookings import router as bookings_router
from app.routes.payments import router as payments_router
from app.routes.reviews import router as reviews_router
from app.routes.favorites import router as favorites_router


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="Hotel Booking API",
    version="1.0.0"
)


# =========================================================
# GZIP COMPRESSION
# =========================================================
# ამცირებს დიდი JSON პასუხების ზომას.
# 500 ბაიტზე დიდი პასუხები ავტომატურად შეიკუმშება.

app.add_middleware(
    GZipMiddleware,
    minimum_size=500
)


# =========================================================
# CORS
# =========================================================
# Local development + Vercel production frontend

app.add_middleware(
    CORSMiddleware,

    allow_origins=[
        "http://127.0.0.1:5501",
        "http://localhost:5501",
        "https://hotel-eta-six.vercel.app",
    ],

    allow_credentials=True,

    allow_methods=[
        "GET",
        "POST",
        "PUT",
        "PATCH",
        "DELETE",
        "OPTIONS",
    ],

    allow_headers=["*"],
)


# =========================================================
# ROUTERS
# =========================================================

app.include_router(auth_router)
app.include_router(hotels_router)
app.include_router(rooms_router)
app.include_router(bookings_router)
app.include_router(payments_router)
app.include_router(reviews_router)
app.include_router(favorites_router)


# =========================================================
# ROOT
# =========================================================

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "Hotel Booking API is running"
    }


# =========================================================
# HEALTH CHECK
# =========================================================
# გამოიყენება server-ის მდგომარეობის შესამოწმებლად.
# მაგალითად:
# https://hotel-backend-qeue.onrender.com/health

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }