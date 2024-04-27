FROM python:3.12

WORKDIR /chat

COPY . /chat

RUN pip install -r requirements.txt

RUN python3 start.py

CMD ["python3", "run.py"]