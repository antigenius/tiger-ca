from dataclasses import dataclass
from datetime import datetime

from src.domain.collection import Collection


@dataclass(frozen=True)
class {{cookiecutter.model_class}}:
    id: str
    created_at: datetime
    updated_at: datetime


@dataclass(frozen=True)
class {{cookiecutter.model_class}}Collection(Collection[{{cookiecutter.model_class}}]):
    values: [{{cookiecutter.model_class}}]
