from app.repositories.base import BaseRepository
from app.unit_of_work.uow import UnitOfWork


class BaseService:

    def __init__(self, uow: UnitOfWork):
        self.uow = uow
