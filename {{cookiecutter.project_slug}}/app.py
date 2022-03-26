import asyncio

from fastapi import FastAPI
from uvicorn import (
    Config,
    Server
)

from src.driver.article_driver import ArticleDriverImpl
from src.interactor.article_interactor import ArticleInteractor
from src.repository.article_repository import ArticleRepositoryImpl
from src.rest.article_resource import ArticleResource

app = FastAPI()

article_resource = ArticleResource(
    article_usecase=ArticleInteractor(
        article_repository=ArticleRepositoryImpl(
            article_driver=ArticleDriverImpl()
        )
    )
)

app.add_route('/', article_resource.index)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    config = Config(app, host='0.0.0.0', log_level='error', port=80, loop=loop)
    server = Server(config)
    loop.run_until_complete(server.serve())
