install:
	poetry install

build:
	./build.sh

start:
	python3 -m gunicorn python-project-52.asgi:application -k uvicorn.workers.UvicornWorker
