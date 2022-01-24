FROM python:3.8-alpine

MAINTAINER Aman Saini

ENV PYTHONUNBUFFERED 1

RUN apk update
RUN apk add --no-cache gcc \
                       openldap \
                       libcurl \
                       gpgme-dev \
                       libc-dev \
    && rm -rf /var/cache/apk/*

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D appuser
USER appuser