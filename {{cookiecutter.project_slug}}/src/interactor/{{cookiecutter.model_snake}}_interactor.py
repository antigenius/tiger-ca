from src.domain.{{cookiecutter.model_snake}} import {{cookiecutter.model_class}}Collection
from src.interface.repository.{{cookiecutter.model_snake}}_repository import {{cookiecutter.model_class}}Repository
from src.interface.usecase.{{cookiecutter.model_snake}}_usecase import {{cookiecutter.model_class}}Usecase


class {{cookiecutter.model_class}}Interactor({{cookiecutter.model_class}}Usecase):
    {{cookiecutter.model_snake}}_repository: {{cookiecutter.model_class}}Repository

    def __init__(self, {{cookiecutter.model_snake}}_repository: {{cookiecutter.model_class}}Repository):
        self.{{cookiecutter.model_snake}}_repository = {{cookiecutter.model_snake}}_repository

    async def get_list(self, page: int) -> {{cookiecutter.model_class}}Collection:
        return await self.{{cookiecutter.model_snake}}_repository.get_list(page)
