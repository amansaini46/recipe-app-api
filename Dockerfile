FROM python:3.8-alpine

MAINTAINER Aman Saini

ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add --no-cache postgresql-client
RUN apk add --no-cache --virtual .tmp-build-deps \
        gcc linux-headers postgresql-dev libc-dev
#        openldap libcurl gpgme-dev && rm -rf /var/cache/apk/*

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN apk del .tmp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D appuser
USER appuser