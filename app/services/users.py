from app.db.repositories.users import UserRepository
from app.db.unit_of_work.uow import UnitOfWork


class BookingService:

    def __init__(
        self,
        uow: UnitOfWork,
        user_repository: UserRepository
    ) -> None:
        self.uow = uow
        self.user_repository = user_repository