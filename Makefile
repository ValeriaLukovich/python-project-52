install:
	poetry install

build:
	./build.sh

start:
	gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker
