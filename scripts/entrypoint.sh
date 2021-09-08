#!/bin/bash

# ./manage.py makemigrations app_name
poetry run poetry python -m manage loaddata db_for_tests
poetry run poetry python -m manage makemigrations
poetry run poetry python -m manage migrate