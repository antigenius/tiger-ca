from dataclasses import dataclass
from typing import (
    Generic,
    List,
    TypeVar
)


T = TypeVar('T')


@dataclass(frozen=True)
class Collection(Generic[T]):
    values: List[T]

    def map(self, func) -> map:
        return map(func, self.values)
