from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.repositories.rooms import RoomRepository
from app.dependencies.stubs import uow_provider, session_provider, booking_repository_provider
from app.db.unit_of_work.uow import UnitOfWork
from app.services.rooms import RoomService


def provide_room_repository(session: AsyncSession = Depends(session_provider)) -> RoomRepository:
    return RoomRepository(session=session)


def get_room_service(
        uow: UnitOfWork = Depends(uow_provider),
        room_repository: RoomRepository = Depends(booking_repository_provider)
) -> RoomService:
    return RoomService(uow=uow, room_repository=room_repository)
