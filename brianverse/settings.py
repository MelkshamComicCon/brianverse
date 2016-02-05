# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

SETTINGS_DIR = os.path.dirname(__file__)
PROJECT_PATH = os.path.join(SETTINGS_DIR, os.pardir)
PROJECT_PATH = os.path.abspath(PROJECT_PATH)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ADMINS = (
    ('Dudley', 'tech@melkshamcomiccon.com'),
)

MANAGERS = ADMINS

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(PROJECT_PATH, 'db.sqlite3'),
#     }
# }

ALLOWED_HOSTS = ['*']

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_ROOT = ''
MEDIA_URL = ''

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/
STATIC_ROOT = ''
STATIC_URL = '/static/'
STATIC_PATH = os.path.join(PROJECT_PATH, 'static')
STATICFILES_DIRS = (
    STATIC_PATH,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


# Template stuff
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_PATH = os.path.join(PROJECT_PATH, 'templates')

TEMPLATE_DIRS = (
    TEMPLATE_PATH,
)

# SECURITY WARNING: keep the secret key used in production secret!
with open('/etc/brianverse.key') as f:
    SECRET_KEY = f.read().strip()

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'brianverse.urls'
WSGI_APPLICATION = 'brianverse.wsgi.application'

INSTALLED_APPS = (
    # 'frontpage',
    # 'about',
    # 'event',
    # 'media',
    # 'store',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'django.contrib.admin',
)
