"""
Django settings for biblio project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""
from configurations import Configuration
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import hashlib
import os
import uuid


def get_secret_key(base_dir='.'):
    def gen_key(key_path):
        with open(key_path, 'w') as key_file:
            key = hashlib.sha512(str(uuid.uuid4()).encode('utf8')).hexdigest()
            key_file.write(key)
        return key

    path = os.path.join(base_dir, '.secret.key')

    try:
        secret_key = open(path).read()
        assert secret_key, "Wrong secret key"
    except (IOError, AssertionError):
        secret_key = gen_key(path)
    return secret_key


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


class Production(Configuration):
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = get_secret_key(BASE_DIR)

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = False

    TEMPLATE_DEBUG = False

    ALLOWED_HOSTS = ['127.0.0.1']


    # Application definition

    INSTALLED_APPS = (
        'shelf',
        'contact',
        'rental',
        'users',
        
        ###################
        
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'django.contrib.sites',
        'bootstrap3',
        
        ###################

        'allauth',
        'allauth.account',
        'allauth.socialaccount',
        'allauth.socialaccount.providers.facebook',

        ###################

    )

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    )

    ROOT_URLCONF = 'biblio.urls'

    WSGI_APPLICATION = 'biblio.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.7/ref/settings/#databases

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }

    # Internationalization
    # https://docs.djangoproject.com/en/1.7/topics/i18n/

    LANGUAGE_CODE = 'pl'

    TIME_ZONE = 'Europe/Warsaw'

    USE_I18N = True  # internationalization

    USE_L10N = True  # localization

    USE_TZ = True

    AUTH_USER_MODEL = 'users.BiblioUser'

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.7/howto/static-files/

    

    TEMPLATE_DIRS = (
        os.path.join(BASE_DIR, 'templates'),
    )

    TEMPLATE_CONTEXT_PROCESSORS = (
        "django.contrib.auth.context_processors.auth",
        "django.core.context_processors.debug",
        "django.core.context_processors.i18n",
        "django.core.context_processors.media",
        "django.core.context_processors.static",
        "django.core.context_processors.tz",
        "django.contrib.messages.context_processors.messages",
        "django.core.context_processors.request",
        "allauth.account.context_processors.account",
        "allauth.socialaccount.context_processors.socialaccount",
    )

    AUTHENTICATION_BACKENDS = (
        'django.contrib.auth.backends.ModelBackend',
        "allauth.account.auth_backends.AuthenticationBackend",
    )

    SITE_ID = 1  # because of 'django.contrib.sites'

    LOGIN_REDIRECT_URL = 'main-page'  # '/'
    
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    STATIC_URL = '/static/'

    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
    
    MEDIA_URL = '/media/'
    
    STATICFILES_DIRS = [
        ("media", os.path.join(BASE_DIR, 'media')),
    ]


class Dev(Production):
    DEBUG = True

    TEMPLATE_DEBUG = True

    EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
