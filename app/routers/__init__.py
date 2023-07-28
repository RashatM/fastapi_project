from fastapi import FastAPI

from app.routers.auth import auth_router
from app.routers.bookings import booking_router
from app.routers.hotels import hotel_router


def setup_routes(app: FastAPI):
    app.include_router(auth_router)
    app.include_router(booking_router)
    app.include_router(hotel_router)
