#!/bin/sh

# waits for db to start
/wait

sleep 10

# migrations
python manage.py migrate --noinput
python manage.py collectstatic --noinput

gunicorn potatoapi.wsgi -b 0.0.0.0:8082 --workers 5 --threads 2

