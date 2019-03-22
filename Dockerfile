FROM python:3.6

ENV DEASY_GUNICORN_NUMBER_OF_WORKERS=2

RUN python -m pip install --upgrade pip

COPY src/requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY src /test

WORKDIR /test

COPY ./docker-entrypoint-api.sh /docker-entrypoint-api.sh

RUN chmod +xxx /docker-entrypoint-api.sh

EXPOSE 8000

ENTRYPOINT ["/docker-entrypoint-api.sh"]