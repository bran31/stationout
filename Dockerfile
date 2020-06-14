FROM python:3.7.4

ENV PYTHONUNBUFFERED 1

RUN mkdir /stationout

WORKDIR /stationout

COPY . . 