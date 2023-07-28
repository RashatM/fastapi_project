from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker

from app.adapters.encrypt_adapter import EncryptionAdapter
from app.dependencies.bookings import provide_booking_repository
from app.dependencies.db import provide_uow
from app.dependencies.hotels import provide_hotel_repository
from app.dependencies.rooms import provide_room_repository
from app.dependencies.stubs import booking_repository_provider, session_provider, auth_provider, encrypt_provider, \
    user_repository_provider, uow_provider, room_repository_provider, hotel_repository_provider
from app.dependencies.users import provide_user_repository
from app.providers.auth_provider import AuthenticationProvider
from app.providers.db_provider import DBProvider


def setup_di(app: FastAPI, pool: async_sessionmaker) -> None:
    db_provider = DBProvider(pool)

    app.dependency_overrides[session_provider] = db_provider.provide_session
    app.dependency_overrides[auth_provider] = AuthenticationProvider
    app.dependency_overrides[encrypt_provider] = EncryptionAdapter
    app.dependency_overrides[uow_provider] = provide_uow
    app.dependency_overrides[user_repository_provider] = provide_user_repository
    app.dependency_overrides[booking_repository_provider] = provide_booking_repository
    app.dependency_overrides[room_repository_provider] = provide_room_repository
    app.dependency_overrides[hotel_repository_provider] = provide_hotel_repository
