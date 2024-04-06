install:
	pip install

build:
	./build.sh

start:
	python3 -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker


migrate:
	poetry run python3 manage.py migrate