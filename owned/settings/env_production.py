# -*- coding: utf-8 -*-
DEBUG = False
TEMPLATE_DEBUG = DEBUG
SERVE_MEDIA = DEBUG

EMAIL_HOST = "in.mailjet.com"
EMAIL_HOST_USER = os.environ.get("MAILJET_USERNAME")
EMAIL_HOST_PASSWORD = os.environ.get("MAILJET_PASSWORD")
EMAIL_USE_TLS = True
EMAIL_PORT = 587
DEFAULT_FROM_EMAIL = 'Owned - Um Novo Jogador <owned@deodoro.org>'