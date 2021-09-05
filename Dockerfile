FROM python:3.9.2-buster
WORKDIR /app
ADD . /app
RUN pip install poetry && poetry install
EXPOSE 8000
CMD ["poetry", "run", "python", "-m", "manage", "runserver", "0.0.0.0:8000"]
