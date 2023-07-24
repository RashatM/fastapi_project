from app.db.repositories.rooms import RoomRepository
from app.db.unit_of_work.uow import UnitOfWork


class RoomService:

    def __init__(
        self,
        uow: UnitOfWork,
        room_repository: RoomRepository
    ):
        self.uow = uow
        self.room_repository = room_repository

