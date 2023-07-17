from dataclasses import dataclass
from typing import Generic, TypeVar

from pydantic import BaseModel

TData = TypeVar("TData")


@dataclass(frozen=True)
class ErrorResult(BaseModel, Generic[TData]):
    message: str
    data: TData
