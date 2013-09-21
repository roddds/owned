import os

ACCOUNT_ACTIVATION_DAYS=7
EMAIL_HOST='smtp.gmail.com'
EMAIL_SERVER='roddds@gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER='roddds@gmail.com'
EMAIL_HOST_PASSWORD=os.environ.get("RODRIGO_PASSWORD")

DEFAULT_FROM_EMAIL = 'Rodrigo Deodoro <roddds@gmail.com>'

# debug code
EMAIL_HOST="localhost"
EMAIL_PORT = 1025
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
EMAIL_USE_TLS = False
DEFAULT_FROM_EMAIL = 'testing@example.com'