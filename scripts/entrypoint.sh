#!/bin/sh

# ./manage.py makemigrations app_name
poetry run python -m manage loaddata db_for_tests
poetry run python -m manage makemigrations
poetry run python -m manage migrate