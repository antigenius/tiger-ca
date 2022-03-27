from fastapi.encoders import jsonable_encoder

from src.domain.{{cookiecutter.model_snake}} import {{cookiecutter.model_class}}Collection
from src.interface.usecase.{{cookiecutter.model_snake}}_usecase import {{cookiecutter.model_class}}Usecase


class {{cookiecutter.model_class}}Resource:
    {{cookiecutter.model_snake}}_usecase: {{cookiecutter.model_class}}Usecase

    def __init__(self, {{cookiecutter.model_snake}}_usecase: {{cookiecutter.model_class}}Usecase):
        self.{{cookiecutter.model_snake}}_usecase = {{cookiecutter.model_snake}}_usecase

    async def index(self):
        main_group: {{cookiecutter.model_class}}Collection = await self.{{cookiecutter.model_snake}}_usecase.get_list(0)
        return jsonable_encoder({{cookiecutter.model_snake}}_collection_response(main_group))


def {{cookiecutter.model_snake}}_collection_response({{cookiecutter.model_snake}}_collection: {{cookiecutter.model_class}}Collection) -> dict:
    return {
        'items': [{
            'id': {{cookiecutter.model_snake}}.id,
            'created_at': {{cookiecutter.model_snake}}.created_at,
            'updated_at': {{cookiecutter.model_snake}}.updated_at
        } for {{cookiecutter.model_snake}} in {{cookiecutter.model_snake}}_collection.values]
    }
