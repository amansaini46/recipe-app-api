FROM python:3.10-alpine

MAINTAINER Aman Saini

ENV PYTHONUNBUFFERED 1

RUN apk update
#RUN apk add --no-cache postgresql-client
#RUN apk add --no-cache --virtual .tmp-build-deps \
#        gcc linux-headers postgresql-dev libc-dev
#        openldap libcurl gpgme-dev && rm -rf /var/cache/apk/*
#RUN apk del .tmp-build-deps

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.txt /tmp/requirements-dev.txt
RUN mkdir /app
WORKDIR /app
COPY ./app /app
EXPOSE 8000

ARG DEV=false

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /tmp/requirements.txt && \
    if [ $DEV = "true" ]; \
    then /py/bin/pip install -r  /tmp/requirements-dev.txt ; \
    fi && \
    rm -rf /tmp && \
    adduser -D -H appuser

ENV PATH="/py/bin:$PATH"

USER appuser