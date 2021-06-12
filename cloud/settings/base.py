"""
Django settings for server project.

Generated by 'django-admin startproject' using Django 3.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path
import os

try:
    import cloud.settings._secrets as secure
    SECRET_KEY_01 = secure.SECRET_KEY_01
    # Configurations for GCP
    #SECRET_KEY_06 = secure.SECRET_KEY_06
    #SECRET_KEY_07 = secure.SECRET_KEY_07
    #SECRET_KEY_08 = secure.SECRET_KEY_08
    #SECRET_KEY_09 = secure.SECRET_KEY_09
    #SECRET_KEY_10 = secure.SECRET_KEY_10
    #SECRET_KEY_11 = secure.SECRET_KEY_11
    # Optional Configurations for Heroku
    DATABASE_URL = secure.DATABASE_URL
except ImportError:
    SECRET_KEY_01 = "error_token"
    # Configurations for GCP
    # SECRET_KEY_06 = "error_token"
    # SECRET_KEY_07 = "error_token"
    # SECRET_KEY_08 = "error_token"
    # SECRET_KEY_09 = "error_token"
    # SECRET_KEY_10 = "error_token"
    # SECRET_KEY_11 = "error_token"
    DATABASE_URL = "error_token"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY_01", SECRET_KEY_01)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1','betatest-api.herokuapp.com','localhost','0.0.0.0']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # my apps
    'cloud',
    'api.apps.ApiConfig',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'cloud.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

AUTH_USER_MODEL = 'api.Account'

WSGI_APPLICATION = 'cloud.wsgi.application'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# for MySQL on GCP:
import pymysql  # noqa: 402
pymysql.version_info = (1, 4, 6, 'final', 0)  # change mysqlclient version
pymysql.install_as_MySQLdb()

# DB Configuration for GCP
#if os.getenv('GAE_APPLICATION', None):
#    # Running on production App Engine, so connect to Google Cloud SQL using the unix socket at /cloudsql/<your-cloudsql-connection string>
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.mysql',
#            'HOST': os.getenv("SECRET_KEY_07", SECRET_KEY_07),
#            'USER': os.getenv("SECRET_KEY_09", SECRET_KEY_09),
#            'PASSWORD': os.getenv("SECRET_KEY_10", SECRET_KEY_10),
#            'NAME': os.getenv("SECRET_KEY_11", SECRET_KEY_11),
#        }
#    }
#else:
#    # *NOTE TO DEVELOPER:
#    # Start the proxy first before trying to run manage.py (saves you a lot of pain trying to figure out why you can't connect to the host when it isn't even OPEN)
#    # Running locally so connect to either a local MySQL instance or connect to Cloud SQL via the proxy. To start the proxy via command line:
#    #
#    #     $ cloud_sql_proxy -instances="amplifyio-308412:asia-southeast1:amplify-io"=tcp:3307 
#    #     (we won't use 3306 since it is already in use by local sql, instead we will use 3307)
#    #
#    # See https://cloud.google.com/sql/docs/mysql-connect-proxy
#    DATABASES = {
#        'default': {
#            'ENGINE': 'django.db.backends.mysql',
#            'HOST': os.getenv("SECRET_KEY_06", SECRET_KEY_06),
#            'PORT': os.getenv("SECRET_KEY_08", SECRET_KEY_08),
#            'USER': os.getenv("SECRET_KEY_09", SECRET_KEY_09),
#            'PASSWORD': os.getenv("SECRET_KEY_10", SECRET_KEY_10),
#            'NAME': os.getenv("SECRET_KEY_11", SECRET_KEY_11),
#        }
#    }

# for postgreSQL on Heroku:
import dj_database_url as herokuDB
import psycopg2

# DB Configuration for Heroku
DATABASES = {}
os.environ['DATABASE_URL'] = os.getenv("DATABASE_URL", DATABASE_URL)
DATABASES['default'] = herokuDB.config()

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# Configuration for GCP Only
# STATIC_ROOT = 'static'

# Configuration for Heroku Only
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)


