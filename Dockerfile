FROM python:3.9.2-buster
WORKDIR /app
ADD . /app
RUN echo $PATH
#ENV PATH="${PATH}:/root/.poetry/bin"

#RUN poetry config virtualenvs.in-project true
#ENV PATH="${PATH}:/usr/local/bin/poetry"
RUN pip install poetry && poetry config virtualenvs.create false && poetry install

#RUN poetry shell
#RUN poetry install
#RUN source $HOME/.poetry/env && poetry update && poetry install
#RUN source $HOME/.poetry/env && poetry install
#RUN ["/bin/sh" ,"-c", "poetry shell"]
#RUN poetry shell
#RUN ["poetry", "shell"]
RUN cd /app/web_calculator/
WORKDIR /app/web_calculator/



EXPOSE 8000
#ENTRYPOINT ["python3", "manage.py"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]


