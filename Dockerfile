FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip3 install --upgrade pip
RUN pip3 install pipenv && pipenv install --system

COPY . /code/

CMD ["gunicorn"  , "--worker-class", "eventlet", "-w", "1", "--bind", "0.0.0.0:8069", "run:app"]
