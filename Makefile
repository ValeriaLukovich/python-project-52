install:
	poetry install

migrate:
	poetry run python manage.py migrate

build:
	./build.sh

start:
	python3 -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker

lint:
	poetry run flake8 task_manager

test:
	poetry run python manage.py test