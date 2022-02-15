FROM python:3.8

RUN mkdir /api

WORKDIR /api

COPY requirements.txt /api/

RUN pip install -r  requirements.txt

COPY . /api/

