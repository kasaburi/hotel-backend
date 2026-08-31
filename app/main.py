
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine

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
# DATABASE
# =========================================================

Base.metadata.create_all(bind=engine)


# =========================================================
# FASTAPI APP
# =========================================================

app = FastAPI(
    title="Hotel Booking API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
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
        "message": "Hotel Booking API is running"
    }


# =========================================================
# HEALTH CHECK
# =========================================================

@app.get("/health")
def health():
    return {
        "status": "ok"
    }