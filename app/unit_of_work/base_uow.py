from abc import ABC, abstractmethod


class BaseUnitOfWork(ABC):

    @abstractmethod
    def commit(self) -> None:
        pass

    @abstractmethod
    def rollback(self) -> None:
        pass

