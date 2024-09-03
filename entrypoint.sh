#!/bin/sh


python manage.py makemigrations
python manage.py migrate --no-input


python manage.py collectstatic --no-input


exec gunicorn --bind 0.0.0.0:8000 payfortech.wsgi:application