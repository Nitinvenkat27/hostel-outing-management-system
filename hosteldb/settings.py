"""
Django settings for hosteldb project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import environ

from qr_code.qrcode import constants

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
env = environ.Env()
environ.Env.read_env()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env("DEBUG") == "False"
# DEBUG = os.environ.get("DEBUG", False)

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'institute',
    'officials',
    'students',
    'complaints',
    'workers',
    'security',
    'django_auth',
    'qr_code',
    'mess_feedback',
    'crispy_bootstrap4',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hosteldb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'Error_Templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'hosteldb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "public",
        'USER': "postgres",
        'PASSWORD': "postgresql",
        'HOST': "localhost",
        'PORT': "5432",
    }
}

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True

AUTH_USER_MODEL = 'django_auth.User'
LOGIN_URL = 'django_auth:login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

CRISPY_TEMPLATE_PACK = 'bootstrap4'

STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'

EMAIL_BACKEND='django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtp.gmail.com'
EMAIL_HOST_USER=env("APP_EMAIL")
EMAIL_HOST_PASSWORD=env("APP_EMAIL_PASSWORD")
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_USE_SSL=False

MEDIA_ROOT= os.path.join(BASE_DIR, 'media/')
MEDIA_URL= "/media/"


if env("ENVIRONMENT") == "development":
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': "public",
        'USER': "postgres",
        'PASSWORD': "postgresql",
        'HOST': "localhost",
        'PORT': "5432",
    }
    }

    AUTH_PASSWORD_VALIDATORS = []
    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Caches.
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    },
    'qr-code': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'qr-code-cache',
        'TIMEOUT': 3600
    }
}

# Django QR Code specific options.
QR_CODE_CACHE_ALIAS = 'qr-code'
QR_CODE_URL_PROTECTION = {
    constants.TOKEN_LENGTH: 30,  # Optional random token length for URL protection. Defaults to 20.
    constants.SIGNING_KEY: 'my-secret-signing-key',  # Optional signing key for URL token. Uses SECRET_KEY if not defined.
    constants.SIGNING_SALT: 'my-signing-salt',  # Optional signing salt for URL token.
    constants.ALLOWS_EXTERNAL_REQUESTS_FOR_REGISTERED_USER: lambda u: True  # Tells whether a registered user can request the QR code URLs from outside a site that uses this app. It can be a boolean value used for any user, or a callable that takes a user as parameter. Defaults to False (nobody can access the URL without the security token).
}
SERVE_QR_CODE_IMAGE_PATH = 'qr-code-image/'

#SECURE_SSL_REDIRECT = True
# CSRF_COOKIE_SECURE = True
# SESSION_COOKIE_SECURE = True
# SECURE_HSTS_SECONDS = 31536000
# SECURE_HSTS_INCLUDE_SUBDOMAINS = True
# SECURE_HSTS_PRELOAD = True