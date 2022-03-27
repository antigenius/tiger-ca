import asyncio

from fastapi import FastAPI
from uvicorn import (
    Config,
    Server
)

from src.driver.{{cookiecutter.model_snake}}_driver import {{cookiecutter.model_class}}DriverImpl
from src.interactor.{{cookiecutter.model_snake}}_interactor import {{cookiecutter.model_class}}Interactor
from src.repository.{{cookiecutter.model_snake}}_repository import {{cookiecutter.model_class}}RepositoryImpl
from src.rest.{{cookiecutter.model_snake}}_resource import {{cookiecutter.model_class}}Resource

app = FastAPI()

{{cookiecutter.model_snake}}_resource = {{cookiecutter.model_class}}Resource(
    {{cookiecutter.model_snake}}_usecase={{cookiecutter.model_class}}Interactor(
        {{cookiecutter.model_snake}}_repository={{cookiecutter.model_class}}RepositoryImpl(
            {{cookiecutter.model_snake}}_driver={{cookiecutter.model_class}}DriverImpl()
        )
    )
)


@app.get('/')
async def index():
    return await {{cookiecutter.model_snake}}_resource.index()


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    config = Config(app, host='0.0.0.0', log_level='error', port=80, loop=loop)
    server = Server(config)
    loop.run_until_complete(server.serve())
