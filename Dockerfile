FROM python:3.11-alpine

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app
COPY requirements.txt  /app/
COPY . /app


EXPOSE 8000
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt




