from sqlalchemy.ext.asyncio import AsyncSession

from app.repositories.users import UserRepository
from app.unit_of_work.base_uow import BaseUnitOfWork


class UnitOfWork(BaseUnitOfWork):

    def __init__(self, session: AsyncSession):
        self._session = session
        self._repositories = {}

    def _get_repository(self, repo_type):
        if repo_type not in self._repositories:
            self._repositories[repo_type] = repo_type(self._session)
        return self._repositories[repo_type]

    @property
    def user_repository(self) -> UserRepository:
        return self._get_repository(UserRepository)

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()

