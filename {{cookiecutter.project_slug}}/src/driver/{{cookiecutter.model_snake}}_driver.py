from datetime import datetime

from src.interface.driver.{{cookiecutter.model_snake}}_driver import {{cookiecutter.model_class}}Driver


class {{cookiecutter.model_class}}DriverImpl({{cookiecutter.model_class}}Driver):
    async def get_{{cookiecutter.model_snake}}_collection(self, page: int) -> dict:
        return {
            '{{cookiecutter.model_snake}}_collection': [{
                'id': 1,
                'created_at': datetime.now(),
                'updated_at': datetime.now()
            }]
        }
