from typing import Dict
from abc import ABC, abstractmethod


class IAuthenticationProvider(ABC):

    @staticmethod
    @abstractmethod
    def create_access_token(data: dict) -> str:
        pass

    @classmethod
    @abstractmethod
    def create_user_token(cls, user_id: int) -> str:
        pass

    @staticmethod
    @abstractmethod
    def decode_token(token: str) -> Dict[str, str]:
        pass

    @classmethod
    @abstractmethod
    def get_token_sub(cls, token: str) -> int:
        pass
