from abc import (
    ABC,
    abstractmethod
)

from src.domain.{{cookiecutter.model_snake}} import {{cookiecutter.model_class}}Collection


class {{cookiecutter.model_class}}Repository(ABC):
    @abstractmethod
    async def get_list(self) -> {{cookiecutter.model_class}}Collection:
        raise NotImplementedError
