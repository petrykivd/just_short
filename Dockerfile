FROM python:3.10-slim-buster
LABEL maitaner="petrykiv.dmytro19@gmail.com"

ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

RUN apt-get update \
    && apt-get -y install libpq-dev gcc \
    && apt-get install -y netcat

COPY . .

RUN mkdir -p /vol/web/media

RUN adduser \
        --disabled-password \
        --no-create-home \
        flask-user

RUN chown -R flask-user:flask-user /vol/
RUN chmod -R 755 /vol/web/

USER flask-user
