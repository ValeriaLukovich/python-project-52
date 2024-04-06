install:
	pip install

build:
	./build.sh

start:
	python -m gunicorn task_manager.asgi:application -k uvicorn.workers.UvicornWorker
	#python manage.py runserver


migrate:
	poetry run python manage.py migrate