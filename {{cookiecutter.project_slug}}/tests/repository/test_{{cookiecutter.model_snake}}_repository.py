from unittest import TestCase
from unittest.mock import AsyncMock

from src.domain.{{cookiecutter.model_snake}} import (
    {{cookiecutter.model_class}},
    {{cookiecutter.model_class}}Collection
)
from src.interface.driver.{{cookiecutter.model_snake}}_driver import {{cookiecutter.model_class}}Driver
from src.repository.{{cookiecutter.model_snake}}_repository import {{cookiecutter.model_class}}RepositoryImpl
from tests import async_test


class DriverMock({{cookiecutter.model_class}}Driver):
    async def get_{{cookiecutter.model_snake}}_collection(self, page: int) -> dict:
        raise NotImplementedError


class Test{{cookiecutter.model_class}}Repository(TestCase):
    @async_test
    async def test_get(self):
        get_main_group_mock = AsyncMock(return_value={"{{cookiecutter.model_snake}}": [
            {"id": "1", "body": "test"}
        ]})

        driver = DriverMock()
        driver.get_{{cookiecutter.model_snake}}_collection = get_main_group_mock
        repository = {{cookiecutter.model_class}}RepositoryImpl({{cookiecutter.model_snake}}_driver=driver)

        self.assertEqual(
            await repository.get_list(1),
            {{cookiecutter.model_class}}Collection(values=[{{cookiecutter.model_class}}(id="1", body="test")])
        )
        get_main_group_mock.assert_called_with(1)
