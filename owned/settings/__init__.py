print "Read", __file__

import os
from .base import *

DJANGO_ENV = os.environ.get('DJANGO_ENV', 'production')


if DJANGO_ENV == 'local':
    from .env_local import *
else:
    from .env_production import *
