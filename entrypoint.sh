#!/bin/sh

# waits for db to start
# /wait

#pipenv run uwsgi --http :8080 -w potatoapi.wsgi
uwsgi --http :8080 -w potatoapi.wsgi --processes 5
