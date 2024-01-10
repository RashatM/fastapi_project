from fastapi import FastAPI
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession

from app.adapters.auth_adapter import AuthenticationAdapter
from app.adapters.encrypt_adapter import EncryptionAdapter
from app.dependencies.providers.bookings import provide_booking_repository, provide_booking_service
from app.dependencies.providers.db import provide_uow, provide_session
from app.dependencies.providers.hotels import provide_hotel_repository, provide_hotel_service
from app.dependencies.providers.rooms import provide_room_repository, provide_room_service
from app.dependencies.stub import Stub
from app.dependencies.providers.users import provide_user_repository, provide_auth_service
from app.interfaces.adapters.encrypt_adapter import IEncryptionAdapter
from app.interfaces.auth_adapter import IAuthenticationAdapter
from app.interfaces.repositories.bookings import IBookingRepository
from app.interfaces.repositories.hotels import IHotelRepository
from app.interfaces.repositories.rooms import IRoomRepository
from app.interfaces.repositories.users import IUserRepository
from app.interfaces.services.auth import IAuthenticationService
from app.interfaces.services.bookings import IBookingService
from app.interfaces.services.hotels import IHotelService
from app.interfaces.services.rooms import IRoomService
from app.interfaces.uow import IUnitOfWork


def setup_di(app: FastAPI) -> None:

    app.dependency_overrides[Stub(async_sessionmaker[AsyncSession])] = lambda: app.state.pool
    app.dependency_overrides[Stub(AsyncSession)] = provide_session
    app.dependency_overrides[Stub(IAuthenticationAdapter)] = AuthenticationAdapter
    app.dependency_overrides[Stub(IEncryptionAdapter)] = EncryptionAdapter
    app.dependency_overrides[Stub(IUnitOfWork)] = provide_uow
    app.dependency_overrides[Stub(IUserRepository)] = provide_user_repository
    app.dependency_overrides[Stub(IBookingRepository)] = provide_booking_repository
    app.dependency_overrides[Stub(IRoomRepository)] = provide_room_repository
    app.dependency_overrides[Stub(IHotelRepository)] = provide_hotel_repository
    app.dependency_overrides[Stub(IAuthenticationService)] = provide_auth_service
    app.dependency_overrides[Stub(IBookingService)] = provide_booking_service
    app.dependency_overrides[Stub(IRoomService)] = provide_room_service
    app.dependency_overrides[Stub(IHotelService)] = provide_hotel_service
