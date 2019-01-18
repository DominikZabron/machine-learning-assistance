FROM python:3

ADD . /app
WORKDIR /app

RUN pip install pipenv
RUN pipenv lock -r >> requirements.txt
RUN pip install -r requirements.txt

COPY . /app

ENV FLASK_APP=api.py