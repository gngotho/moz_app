"""
Django settings for challenge project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

PROJECT_ROOT = os.path.dirname(__file__)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')5zsk!+*&l#rq5#&v^l$xm(d8skhio%&h51c6y^%sw1jtgrcsg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['*']

STATIC_ROOT = os.path.join(
 os.path.dirname(
  os.path.dirname(
   os.path.abspath(__file__))), 'static')
# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'polygonapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'challenge.urls'

WSGI_APPLICATION = 'challenge.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases
if 'RDS_DB_NAME' in os.environ:
    DATABASES = {
    'default': {
    'ENGINE': 'django.contrib.gis.db.backends.mysql',
    'NAME': os.environ['RDS_DB_NAME'],
    'USER': os.environ['RDS_USERNAME'],
    'PASSWORD': os.environ['RDS_PASSWORD'],
    'HOST': os.environ['RDS_HOSTNAME'],
    'PORT': os.environ['RDS_PORT'],
  }
 }

else:
    DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.mysql',
        'NAME': 'challenge',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'root',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',     
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'challenge', 'templates'),
)

STATIC_URL = '/static/'

# static media
#STATIC_ROOT                         = os.path.join(BASE_DIR, 'static')
STATIC_URL                          = '/static/'
STATICFILES_DIRS                    = (
    os.path.join(BASE_DIR, 'polygonapp', 'static', 'static'),
    os.path.join(BASE_DIR, 'challenge', 'static'),
)
