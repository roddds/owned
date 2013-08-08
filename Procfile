#web: newrelic-admin run-program python manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
#celeryd: python manage.py celeryd -E -B --settings=settings --loglevel=INFO

web: python manage.py run_gunicorn -b "0.0.0.0:$PORT" -w 3
celeryd: python manage.py celery worker --loglevel=info

