from abc import ABC, abstractmethod



class IEncryptionAdapter(ABC):

    @staticmethod
    @abstractmethod
    def get_password_hash(password: str) -> str:
        pass

    @staticmethod
    @abstractmethod
    def verify_password(plain_password, hashed_password) -> bool:
        pass
