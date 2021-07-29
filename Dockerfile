FROM python:3.9.2
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install poetry
RUN poetry install
EXPOSE 8000
CMD python manage.py runserver 8000



