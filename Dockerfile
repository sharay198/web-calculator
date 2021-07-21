FROM python:3.9.2
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install poetry
RUN poetry install

CMD python manage.py runserver 127.0.0.1:8000



