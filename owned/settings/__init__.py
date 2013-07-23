import os

DJANGO_ENV = os.environ.get('DJANGO_ENV', 'local')

if DJANGO_ENV == 'local':
    from .env_local import *