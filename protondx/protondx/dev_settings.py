"""
Overrides production settings with development values.
"""

ALLOWED_HOSTS = []
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'sample_database',
        'USER': 'oliver_django',
        'PASSWORD': '1234567T',
        'HOST': 'localhost',
        'PORT': '',
    }
}