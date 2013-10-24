import os

ACCOUNT_ACTIVATION_DAYS=7

if os.environ.get('DJANGO_ENV', 'local') == 'production':
    EMAIL_HOST = "in.mailjet.com"
    EMAIL_HOST_USER = os.environ.get("MAILJET_USERNAME")
    EMAIL_HOST_PASSWORD = os.environ.get("MAILJET_PASSWORD")
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    DEFAULT_FROM_EMAIL = 'Owned - Um Novo Jogador <owned@deodoro.org>'
else:
    EMAIL_HOST="localhost"
    EMAIL_PORT = 1025
    EMAIL_USE_TLS = False
    EMAIL_HOST_USER = ""
    EMAIL_HOST_PASSWORD = ""
    DEFAULT_FROM_EMAIL = 'testing@example.com'

