# -*- coding: utf-8 -*-
import os
import sys
from unipath import Path
from datetime import datetime

from .django import *
from .email import *


PROJECT_DIR = Path(__file__).parent.parent

sys.path.append(PROJECT_DIR.child('apps'))
sys.path.append(PROJECT_DIR.child('libs'))


STATICFILES_DIRS = ( PROJECT_DIR.child('static'), )
FIXTURE_DIRS = ( PROJECT_DIR.child('static'), )

AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'lazysignup.backends.LazySignupBackend')