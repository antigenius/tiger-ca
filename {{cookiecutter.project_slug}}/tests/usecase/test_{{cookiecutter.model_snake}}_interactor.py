from unittest import TestCase
from unittest.mock import AsyncMock

from src.domain.{{cookiecutter.model_snake}} import (
    {{cookiecutter.model_class}},
    {{cookiecutter.model_class}}Collection
)
from src.interactor.{{cookiecutter.model_snake}}_interactor import {{cookiecutter.model_class}}Interactor
from src.interface.repository.{{cookiecutter.model_snake}}_repository import {{cookiecutter.model_class}}Repository
from tests import async_test


class RepositoryMock({{cookiecutter.model_class}}Repository):
    async def get_list(self, page: str) -> {{cookiecutter.model_class}}Collection:
        raise NotImplementedError


class Test{{cookiecutter.model_class}}Interactor(TestCase):
    @async_test
    async def test_get(self):
        get_mock = AsyncMock(
            return_value={{cookiecutter.model_class}}(id="1", body='test'))

        repo = RepositoryMock()
        repo.get_list = get_mock
        usecase = {{cookiecutter.model_class}}Interactor({{cookiecutter.model_snake}}_repository=repo)

        self.assertEqual(await usecase.get_list(1), {{cookiecutter.model_class}}(id="1", body="test"))
        get_mock.assert_called_with(1)
