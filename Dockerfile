FROM python:3.11-alpine

WORKDIR /app

COPY . .

EXPOSE 5000

RUN apk update && apk --no-cache --update add build-base

RUN pip install poetry