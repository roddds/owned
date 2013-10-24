import os

ACCOUNT_ACTIVATION_DAYS=7

EMAIL_HOST="localhost"
EMAIL_PORT = 1025
EMAIL_USE_TLS = False
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
DEFAULT_FROM_EMAIL = 'testing@example.com'

if os.environ.get("DJANGO_ENV", "local"):
    EMAIL_HOST='smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_SERVER='roddds@gmail.com'
    EMAIL_USE_TLS = True
    EMAIL_HOST_USER='roddds@gmail.com'
    EMAIL_HOST_PASSWORD=os.environ.get("RODRIGO_PASSWORD")
    DEFAULT_FROM_EMAIL = 'Rodrigo Deodoro <roddds@gmail.com>'