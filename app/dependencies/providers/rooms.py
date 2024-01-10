from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession


from app.db.repositories.rooms import RoomRepository
from app.dependencies.stub import Stub
from app.interfaces.repositories.hotels import IHotelRepository
from app.interfaces.repositories.rooms import IRoomRepository
from app.interfaces.uow import IUnitOfWork
from app.services.rooms import RoomService


def provide_room_repository(session: AsyncSession = Depends(Stub(AsyncSession))) -> RoomRepository:
    return RoomRepository(session=session)


def provide_room_service(
        uow: IUnitOfWork = Depends(Stub(IUnitOfWork)),
        room_repository: IRoomRepository = Depends(Stub(IRoomRepository)),
        hotel_repository: IHotelRepository = Depends(Stub(IHotelRepository))
) -> RoomService:
    return RoomService(uow=uow, room_repository=room_repository, hotel_repository=hotel_repository)
