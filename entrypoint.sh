#!/bin/sh

# waits for db to start
# /wait

#pipenv run uwsgi --http :8080 -w potatoapi.wsgi
gunicorn potatoapi.wsgi -b 0.0.0.0:8080 --workers 5 --threads 2 --timeout 3600
#python manage.py runserver 0.0.0.0:8080
