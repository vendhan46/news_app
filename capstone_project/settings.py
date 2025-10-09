"""
Django settings for capstone_project project.
"""

from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

# -------------------------------
# ✅ SECURITY SETTINGS
# -------------------------------

SECRET_KEY = os.getenv('SECRET_KEY', 'django-insecure-zpewa@--va+d&#4-m7fs09r6p=xc^9-7c&a3r038#posba&n&-')

DEBUG = os.getenv('DEBUG', 'True') == 'True'

# When you deploy to Render or any host, update this:
ALLOWED_HOSTS = ['*']  # later, change '*' to your Render domain (e.g. 'news-app.onrender.com')


# -------------------------------
# ✅ APPLICATIONS
# -------------------------------
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'appmain',
]

# -------------------------------
# ✅ MIDDLEWARE
# -------------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    # ✅ Added Whitenoise Middleware (must be right below SecurityMiddleware)
    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


ROOT_URLCONF = 'capstone_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
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

WSGI_APPLICATION = 'capstone_project.wsgi.application'


# -------------------------------
# ✅ DATABASE
# -------------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# -------------------------------
# ✅ PASSWORD VALIDATION
# -------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# -------------------------------
# ✅ INTERNATIONALIZATION
# -------------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True


# -------------------------------
# ✅ STATIC & MEDIA FILES
# -------------------------------

# Static URL for development
STATIC_URL = '/static/'

# The directory where `collectstatic` will collect all static files for production
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Optional extra static files in development
STATICFILES_DIRS = [BASE_DIR / 'static']

# Whitenoise storage for production static serving
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# -------------------------------
# ✅ SESSION CONFIGURATION
# -------------------------------
SESSION_EXPIRE_AT_BROWSER_CLOSE = True


# -------------------------------
# ✅ EMAIL SETTINGS
# -------------------------------
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'vendhanvelusamy@gmail.com'  # Replace with your email
EMAIL_HOST_PASSWORD = 'mcde mahg exmq uotc'    # App password (safe only if used as env var)


# -------------------------------
# ✅ DEFAULTS
# -------------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
