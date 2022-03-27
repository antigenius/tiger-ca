from abc import (
    ABC,
    abstractmethod
)

from src.domain.{{cookiecutter.model_snake}} import {{cookiecutter.model_class}}Collection


class {{cookiecutter.model_class}}Usecase(ABC):
    @abstractmethod
    async def get_list(self, page: int) -> {{cookiecutter.model_class}}Collection:
        raise NotImplementedError
