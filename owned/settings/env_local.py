# -*- coding: utf-8 -*-
from .base import *


DEBUG = True
TEMPLATE_DEBUG = True
SERVE_MEDIA = True

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_DIR.child('static_root')
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"

MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_DIR.child('media')

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
