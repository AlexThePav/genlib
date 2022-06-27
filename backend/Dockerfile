FROM python:3.10.1-bullseye

COPY ./requirements.txt /requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r /requirements.txt

RUN mkdir /app
WORKDIR /app
COPY . /app
