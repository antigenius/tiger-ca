run:
	poetry run python app.py

poetry-self-install:
	curl -sSL https://raw.githubusercontent.com/sdispater/poetry/master/get-poetry.py | python

poetry-setup:
	poetry update && poetry install

test-all: poetry-setup
	poetry run pytest ./tests

test-unit: poetry-setup
	poetry run pytest  ./tests/unit

test-dumb:
	poetry run pytest  ./tests
