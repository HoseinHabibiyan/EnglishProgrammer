import os
from pathlib import Path  
from datetime import timedelta
from typing import List, Tuple


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-9suvc13+z^mk!7g(!*x&a0csl7^dhik=c1yt$h$i4h4opo$jt@'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [    
    'English.Merkousha.ir',
    'localhost',
    '127.0.0.1',
    '46.249.100.108',
    ]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Programmer',
    'crispy_forms',
    'crispy_bootstrap5',
    'tinymce',
    'storages',
    'minio_storage'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'EnglishProgrammer.urls'

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
                'Programmer.context_processors.categories',
            ],
        },
    },
]

WSGI_APPLICATION = 'EnglishProgrammer.wsgi.application'


# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
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

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'
STATIC_ROOT = './static_files/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'Programmer/static'),
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


#Crispy forms configuration
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
]

# MEDIA_URL = "/media/"
# MEDIA_ROOT = BASE_DIR / "Programmer/templates/media"

FILE_UPLOAD_MAX_MEMORY_SIZE = 104857600  # 100 MB in bytes



################################################################
###################S3 Configurations
################################################################
AWS_QUERYSTRING_AUTH = False

DEFAULT_FILE_STORAGE = 'minio_storage.storage.MinioMediaStorage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STORAGES = {"default": {"BACKEND": "storages.backends.s3boto3.S3Boto3Storage"}}

AWS_S3_ENDPOINT_URL = 'https://storage.iran.liara.space'
AWS_S3_ACCESS_KEY_ID = 'm2prko9o0vhacb7n'
AWS_S3_SECRET_ACCESS_KEY = 'a556090f-756f-4d42-88f6-531c580a0108'
AWS_STORAGE_BUCKET_NAME = 'refhub'

MINIO_STORAGE_ENDPOINT = 'storage.iran.liara.space'
MINIO_STORAGE_ACCESS_KEY = 'm2prko9o0vhacb7n'
MINIO_STORAGE_SECRET_KEY = 'a556090f-756f-4d42-88f6-531c580a0108'
MINIO_SECRET_KEY = 'a556090f-756f-4d42-88f6-531c580a0108'
MINIO_STORAGE_MEDIA_BUCKET_NAME = 'refhub'


MINIO_STORAGE_USE_HTTPS = True
MINIO_STORAGE_MEDIA_OBJECT_METADATA = {"Cache-Control": "max-age=1000"}
MINIO_CONSISTENCY_CHECK_ON_START = True
MINIO_QUERYSTRING_AUTH = False
MINIO_REGION = 'us-east-1'  # Default is set to None
MINIO_PRIVATE_BUCKETS = [
    # 'django-backend-dev-private',
]
MINIO_PUBLIC_BUCKETS = [
    'refhub',
]
MINIO_URL_EXPIRY_HOURS = timedelta(days=1)  # Default is 7 days (longest) if not defined


# STATIC_URL = f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/static/'
# MEDIA_URL =  f'{AWS_S3_ENDPOINT_URL}/{AWS_STORAGE_BUCKET_NAME}/media/'

STATIC_URL = '/static_files/'
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR 