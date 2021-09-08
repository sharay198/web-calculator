FROM python:3.9.2-buster
WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .
RUN pip install poetry && poetry install
RUN chmod a+x ./scripts/entrypoint.sh

EXPOSE 8000
ADD . /app
COPY scripts/entrypoint.sh /app/scripts/entrypoint.sh
CMD ["./scripts/entrypoint.sh"]
#CMD ["poetry", "run", "python", "-m", "manage", "runserver", "0.0.0.0:8000"]
