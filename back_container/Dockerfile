FROM python:3.9-slim-buster

WORKDIR /back

COPY . .

RUN pip install flask flask_cors requests mysql-connector-python

CMD ["python", "back.py"]