# This is an example localsettings.py file for django-ca. Also see
#   http://django-ca.readthedocs.org/en/latest/settings.html
# for more information.

import os

# BASEDIR is the directory above this file, where your manage.py file is located.
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

STATIC_ROOT = os.path.join(BASE_DIR, "static")

DEBUG = True
# configure your database here:
#DATABASES = {
#    'default': {
#        # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#        'ENGINE': 'django.db.backends.',
#        'NAME': '',
#        'USER': '',
#        'PASSWORD': '',
#        'HOST': '',
#        'PORT': '',
#    }
#}

# This should be long, random and unique:
SECRET_KEY = 'B0F67156-BF19-4898-8685-E54806A17521'

# Hostnames under which this project will be available. This setting is only required if you want
# to run the admin webinterface.
#ALLOWED_HOSTS = [
#   'ca.example.com',
#]

# Where static files (CSS/JavaScript/...) should be collected to. This setting is only required if
# you want to run the admin webinterface.
#STATIC_ROOT = '/var/www/ca.example.com/static'

##################
### CA options ###
##################
# The directory where your CA files are located
#CA_DIR = os.path.join(BASE_DIR, 'files')

# Do not provide a generic CRL view.
#CA_PROVIDE_GENERIC_CRL = False

# OCSP configuration, for more information please see:
#   http://django-ca.readthedocs.io/en/latest/ocsp.html
#CA_OCSP_URLS = {
#    'myca': {
#        'ca': '<serial>',
#        'responder_key': '/path/to/responder.key',
#        'responder_cert': '<serial>',  # could also be a filesystem path
#    }
#}

###########################
### Certificate options ###
###########################
# The default algorithm used for signing certificates.
#CA_DIGEST_ALGORITHM = 'sha512'

# Override any existing CA profiles.
#CA_PROFILES = {}

# Default time in days for signed certificates to expire.
#CA_DEFAULT_EXPIRES = getattr(settings, 'CA_DEFAULT_EXPIRES', 730)

# Default profile used for signing certificates.
#CA_DEFAULT_PROFILE = getattr(settings, 'CA_DEFAULT_PROFILE', 'webserver')

# Notify certificate watchers before certificates expire. This is a list of days before expiration
# that watchers will get an email, in this example 14, seven, three and one days before expiry.
#CA_NOTIFICATION_DAYS = [14, 7, 3, 1, ]
