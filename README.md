### Hexlet tests and linter status:
[![Actions Status](https://github.com/ValeriaLukovich/python-project-52/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ValeriaLukovich/python-project-52/actions)

<a href="https://codeclimate.com/github/ValeriaLukovich/python-project-52/maintainability"><img src="https://api.codeclimate.com/v1/badges/e6b7930e584e69108b42/maintainability" /></a>

<a href="https://codeclimate.com/github/ValeriaLukovich/python-project-52/test_coverage"><img src="https://api.codeclimate.com/v1/badges/e6b7930e584e69108b42/test_coverage" /></a>

https://python-project-52-1.onrender.com

# TASK MANAGER

![Alt text](<Screenshot 2024-05-02 at 16.49.24.png>)

Task Manager – task management system. It allows you to set tasks, assign performers and change their statuses.

This project was build using these tools:
1. python 3.11.8
2. poetry 1.7.1
3. flake8 7.0.0

It will be comfortable to use this application with these commands:
- to install: `pip install --user git@github.com:ValeriaLukovich/python-project-52.git`
- to assemble package : `make build`
- to run app : `make start`
- to run pytest : `make test`
- to run linter : `make lint`

To use the app properly you'll need to provide it with $DATABASE_URL and $SECRET_KEY vars.