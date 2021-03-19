#!/bin/sh

echo "Migrate Schemas"
python manage.py migrate
echo "Collect staticfiles"
python manage.py collectstatic --no-input
echo "Gunicorn"
gunicorn core.wsgi:application -c ./config/gunicorn/conf.py --bind 0.0.0.0:8000