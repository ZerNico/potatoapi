"""
Django settings for potatoapi project.
"""

import os
import environ
root = environ.Path(__file__) - 2
env = environ.Env(DEBUG=(bool, False),)
environ.Env.read_env()


BASE_DIR = root()

DEBUG = env('DEBUG')  # False if not in os.environ
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

ALLOWED_HOSTS = ['127.0.0.1', '0.0.0.0', 'localhost', 'api.potatoproject.co']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_cleanup.apps.CleanupConfig',
    'django_better_admin_arrayfield',
    'rest_framework',
    'rest_framework.authtoken',
    'django_filters',
    'corsheaders',
    'user',
    'blog',
    'ota',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'potatoapi.urls'

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

WSGI_APPLICATION = 'potatoapi.wsgi.application'


# Database

DATABASES = {
    'default': env.db(),  # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
}


# Password validation

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

public_root = root.path('public/')

STATIC_URL = '/public/static/'
STATIC_ROOT = public_root('static')

MEDIA_URL = '/public/media/'
MEDIA_ROOT = public_root('media')

AUTH_USER_MODEL = 'user.User'

REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 1000
}

CORS_ORIGIN_ALLOW_ALL = True
