FROM python:3.9

ADD redis_test_script.py /
RUN pip install redis

CMD [ "python3", "./redis_test_script.py" ]
