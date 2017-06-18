"""
Django settings for Coffee project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key a secret
SECRET_KEY = '_34saw!bco()q8$4(_5iyik-+nmr+u7jrsfywjq)guc9+j%==c'

ALLOWED_HOSTS = ['127.0.0.1', '10346756.ngrok.io', 'starbex.herokuapp.com']
SITE_ID = 3

# Application definitions
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'django_forms_bootstrap',
    'home',
    'accounts',
    'paypal_store',
    'paypal.standard.ipn',
    'coffees',
    'disqus',
    'tinymce',
    'emoticons',
    'threads',
    'polls',
    'blog',
]

AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = ('django.contrib.auth.backends.ModelBackend',
                           'accounts.backends.EmailAuth',)
LOGIN_URL = '/login/'

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware'
]

ROOT_URLCONF = 'Coffee_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'Coffee_project.wsgi.application'

# Password validation (https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators)

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

# Internationalization (https://docs.djangoproject.com/en/1.9/topics/i18n/)

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images) (https://docs.djangoproject.com/en/1.9/howto/static-files/)
STATIC_URL = '/static/'
STATIC_ROOT = ''
STATICFILES_DIRS = (
    # Static Directory at the project level
    os.path.join(BASE_DIR, "static"),
)

# Path to Images
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

# Tinymce Settings
TINYMCE_JS_ROOT = os.path.join(BASE_DIR, "static", 'js', 'tinymce', 'tinymce.min.js')

# Disqus Settings
DISQUS_WEBSITE_SHORTNAME = 'starbex'
