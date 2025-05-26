FROM python:3.8.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

RUN apt-get update && \
    apt-get install -y vim default-libmysqlclient-dev && \
    apt-get clean

ADD requirements.txt /code/
RUN pip install --upgrade pip && pip install -r requirements.txt

ADD . /code/

