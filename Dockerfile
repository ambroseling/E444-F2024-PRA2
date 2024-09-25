# Use an official Python runtime as a base image
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt


COPY . .
ENV FLASK_APP=hello.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=3000
EXPOSE 3000

CMD ["flask","run"]
