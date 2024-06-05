FROM python:3.12

WORKDIR /code

COPY /code /code
COPY requirements.txt /code

RUN pip install -r requirements.txt


RUN python3 start.py

CMD [ "python3", 'run.py']

