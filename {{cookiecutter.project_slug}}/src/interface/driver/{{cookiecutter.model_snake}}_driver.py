from abc import (
    ABC,
    abstractmethod
)


class {{cookiecutter.model_class}}Driver(ABC):
    @abstractmethod
    async def get_{{cookiecutter.model_snake}}_collection(self, page: int) -> dict:
        raise NotImplementedError
