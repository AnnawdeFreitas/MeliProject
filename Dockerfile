FROM ubuntu:latest
LABEL authors="Anna Waleska"

FROM python:3.13.7

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir pytest

CMD ["python", "sum_by_letter.py"]