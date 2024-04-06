install:
	pip install

build:
	./build.sh

start:
	poetry run python3 manage.py runserver 0.0.0.0:8000


migrate:
	poetry run python3 manage.py migrate