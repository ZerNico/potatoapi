#!/bin/sh

# waits for db to start
/wait

sleep 10

# migrations
python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic

gunicorn potatoapi.wsgi -b 0.0.0.0:8082 --workers 5 --threads 2

