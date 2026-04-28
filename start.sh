#!/bin/bash

# 1. Wait for MySQL to be ready
echo "Waiting for MySQL..."
while ! python -c "import MySQLdb; MySQLdb.connect(host='db', user='smp_user', passwd='smp_password', db='smp_db')" ; do
  sleep 1
done
echo "MySQL is up!"

# 2. Run migrations
echo "Running migrations..."
python manage.py migrate --noinput

# 3. Start Gunicorn
echo "Starting Gunicorn..."
exec gunicorn student_management.wsgi:application --bind 0.0.0.0:8000
