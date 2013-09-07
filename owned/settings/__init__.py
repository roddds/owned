print "Read", __file__
import os

DJANGO_ENV = os.environ.get('DJANGO_ENV', 'local')

from .base import *

if DJANGO_ENV == 'local':
    from .env_local import *
else:
    from .env_production import *
