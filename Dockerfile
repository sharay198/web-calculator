FROM python:3.9.2-buster
WORKDIR /app
COPY pyproject.toml .
COPY poetry.lock .
#COPY scripts/entrypoint.sh .
#RUN chmod a+x entrypoint.sh
RUN pip install poetry && poetry install
EXPOSE 8000
COPY . /app
#RUN cd scripts && chmod a+x entrypoint.sh

#&& ./scripts/entrypoint.sh
#RUN poetry run python -m manage migrate
#RUN poetry run python -m manage makemigrations && poetry run python -m manage migrate
#CMD ["poetry", "run", "python", "-m", "manage", "runserver", "0.0.0.0:8000"]