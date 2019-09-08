#!/bin/sh

# waits for db to start
/wait

gunicorn potatoapi.wsgi -b 0.0.0.0:8080 --workers 5 --threads 2 --timeout 3600

