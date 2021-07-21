FROM python:3.9.2
RUN mkdir /app
WORKDIR /app
ADD . /app
RUN pip install django
RUN pip install fast_bitrix24
RUN pip install dadata

CMD python manage.py runserver 127.0.0.1:8000



