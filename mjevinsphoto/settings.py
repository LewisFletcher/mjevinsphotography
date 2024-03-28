from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']

AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']

AWS_STORAGE_BUCKET_NAME = 'mjevissphoto-media'

CSRF_COOKIE_SECURE = True

SESSION_COOKIE_SECURE = True

SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = ['https://meljevinsphotography.co.uk', 'https://www.meljevinsphotography.co.uk']

DEBUG = False

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ADMINS = [('lewis', 'lew.fletcher3@gmail.com')]

ALLOWED_HOSTS = ['.meljevinsphotography.co.uk',]

SECURE_HSTS_SECONDS = 300

SECURE_HSTS_INCLUDE_SUBDOMAINS = True

SECURE_HSTS_PRELOAD = True

SECURE_CONTENT_TYPE_NOSNIFF = True

SECURE_BROWSER_XSS_FILTER = True

X_FRAME_OPTIONS = 'DENY'

# Application definition

TAILWIND_APP_NAME = 'theme'

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Dependencies
    'tailwind',
    'theme',
    #'django_browser_reload',
    #"debug_toolbar",
    "storages",
    "django_htmx",
    
    # My Apps
    'home.apps.HomeConfig',
    'about.apps.AboutConfig',
    'portfolio.apps.PortfolioConfig',
    'packages.apps.PackagesConfig',
    'testimony'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "django_htmx.middleware.HtmxMiddleware",
    #"django_browser_reload.middleware.BrowserReloadMiddleware",
    #"debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = 'mjevinsphoto.urls'

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

WSGI_APPLICATION = 'mjevinsphoto.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}




# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

import dj_database_url
db_from_env = dj_database_url.config(conn_max_age=500)
DATABASES['default'].update(db_from_env)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"
MEDIA_URL = 'https://d2ep2kfwpl2a2s.cloudfront.net/'
AWS_S3_CUSTOM_DOMAIN = 'd2ep2kfwpl2a2s.cloudfront.net'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media').replace('\\', '/')
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
STORAGES = {
    # ...
    "static": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}