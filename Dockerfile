FROM python:3.9.2-buster
WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry && poetry install
EXPOSE 8000
COPY . /app
CMD ["poetry", "run", "python", "-m", "manage", "runserver", "0.0.0.0:8000"]