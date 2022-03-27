from src.domain.{{cookiecutter.model_snake}} import (
    {{cookiecutter.model_class}},
    {{cookiecutter.model_class}}Collection
)
from src.interface.driver.{{cookiecutter.model_snake}}_driver import {{cookiecutter.model_class}}Driver
from src.interface.repository.{{cookiecutter.model_snake}}_repository import {{cookiecutter.model_class}}Repository


class {{cookiecutter.model_class}}RepositoryImpl({{cookiecutter.model_class}}Repository):
    {{cookiecutter.model_snake}}_driver: {{cookiecutter.model_class}}Driver

    def __init__(self, {{cookiecutter.model_snake}}_driver: {{cookiecutter.model_class}}Driver):
        self.{{cookiecutter.model_snake}}_driver = {{cookiecutter.model_snake}}_driver

    async def get_list(self, page: int) -> {{cookiecutter.model_class}}Collection:
        res = await self.{{cookiecutter.model_snake}}_driver.get_{{cookiecutter.model_snake}}_collection(page)
        return {{cookiecutter.model_class}}Collection(
            values=[
                {{cookiecutter.model_class}}(
                    id=r['id'], created_at=r['created_at'], updated_at=r['updated_at'])
                for r in res['{{cookiecutter.model_snake}}_collection']
            ]
        )
