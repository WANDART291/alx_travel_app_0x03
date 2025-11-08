import os
from pathlib import Path
import sys
import dj_database_url

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Ensure project root is in path
sys.path.insert(0, str(BASE_DIR)) 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'

# Correct way to handle ALLOWED_HOSTS for Render
ALLOWED_HOSTS = [os.environ.get('RENDER_EXTERNAL_HOSTNAME'), '127.0.0.1']
# The explicit RENDER_EXTERNAL_HOSTNAME check below is redundant if the above is used, but safe to keep:
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME and RENDER_EXTERNAL_HOSTNAME not in ALLOWED_HOSTS:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'drf_yasg',
    'listings.apps.ListingsConfig',
    'corsheaders',  # <--- RECOMMENDED: Add for API security/access
]

# ⚠️ CRITICAL FIX: Ensure Middleware is a list and WhiteNoise is correctly placed.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Place WhiteNoise first after SecurityMiddleware
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'corsheaders.middleware.CorsMiddleware', # <--- RECOMMENDED: CORS middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'alx_travel_app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'alx_travel_app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.2/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        # Uses the DATABASE_URL environment variable on Render
        default=os.environ.get('DATABASE_URL'),
        conn_max_age=600
    )
}


# Password validation... (omitted for brevity, assume unchanged)
# Internationalization... (omitted for brevity, assume unchanged)


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.2/howto/static-files/

STATIC_URL = 'static/'

# 🚀 CRITICAL FOR PRODUCTION: Static file configuration with WhiteNoise
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Make sure your main app's static files are found
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'alx_travel_app/static') 
]
# Use the compressed and manifest storage for efficiency
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Default primary key field type... (omitted for brevity, assume unchanged)

# CELERY CONFIGURATION (Updated for Redis on Render)

# ⚠️ Use CELERY_BROKER_URL environment variable for flexibility.
# ⚠️ If you deploy a Redis instance on Render, its internal connection string
#    will look like 'redis://<user>:<password>@<host>:<port>'. 
#    We use this variable name for the internal connection string.
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL') 

# Set the result backend to the same broker (best practice for simplicity)
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'UTC'


# EMAIL CONFIGURATION (Required for testing notifications)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT') 
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', 'True').lower() == 'true'
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')


# DRF YASG/SWAGGER CONFIGURATION

SWAGGER_SETTINGS = {
    'USE_SESSION_AUTH': False,
    'SECURITY_DEFINITIONS': {
        'Bearer': {
            'type': 'apiKey',
            'name': 'Authorization',
            'in': 'header'
        }
    }
}
