install:
	poetry install

migrate:
	poetry run python manage.py migrate

build:
	./build.sh

start:
	python3 -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker