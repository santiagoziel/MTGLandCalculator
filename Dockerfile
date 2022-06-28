FROM python:3.9

WORKDIR /code

COPY Pipfile Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv && pipenv install --system

COPY . /code

CMD ["python3", "./run.py"]
