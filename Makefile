install:
	poetry install

build:
	./build.sh

start:
	python -m gunicorn python-project-52.asgi:application -k uvicorn.workers.UvicornWorker
