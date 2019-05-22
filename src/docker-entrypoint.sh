#!/bin/sh
python manage.py collectstatic --noinput
python manage.py makemigrations --noinput
until python manage.py migrate --no-input; do
  >&2 echo "Postgres database is unavailable - sleeping"
  sleep 1
done
gunicorn test_task.wsgi:application --workers $DEASY_GUNICORN_NUMBER_OF_WORKERS --bind :8000
