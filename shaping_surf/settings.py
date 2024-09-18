"""
Django settings for shaping_surf project.

Generated by 'django-admin startproject' using Django 3.2.25.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

import os
import dj_database_url

if os.path.isfile("env.py"):
    import env

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
# Set DEBUG based on environment variable in env.py
DEBUG = "DEV" in os.environ

ALLOWED_HOSTS = [
    "8000-gomarsdotti-shapingsust-h0kchpxwruz.ws.codeinstitute-ide.net",
    "https://8000-gomarsdotti-shapingsust-h0kchpxwruz.ws.codeinstitute-ide.net/",
    "localhost",
    "127.0.0.1",
    "shaping-sustainable-surf-8794b08a1b3a.herokuapp.com",
]

CSRF_TRUSTED_ORIGINS = [
    "https://8000-gomarsdotti-shapingsust-h0kchpxwruz.ws.codeinstitute-ide.net/",
    "https://shaping-sustainable-surf-8794b08a1b3a.herokuapp.com",
    "https://*.codeinstitute-ide.net",
    "https://*.gitpod.io",
]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    "allauth",
    "allauth.account",
    # Apps
    "about",
    "cart",
    "checkout",
    "contact",
    "home",
    "newsletter",
    "products",
    "profiles",
    # Third-party apps
    "autoslug",
    "cloudinary",
    "cloudinary_storage",
    "crispy_forms",
    "crispy_bootstrap4",
    "django_extensions",
    "django_resized",
    "django_summernote",
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"
CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "shaping_surf.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
            os.path.join(BASE_DIR, "templates", "allauth"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "cart.contexts.cart_contents",
            ],
            "builtins": [
                "crispy_forms.templatetags.crispy_forms_tags",
                "crispy_forms.templatetags.crispy_forms_field",
            ],
        },
    },
]

# Necessary in Gitpod for toasts
MESSAGE_STORAGE = "django.contrib.messages.storage.session.SessionStorage"

AUTHENTICATION_BACKENDS = [
    # Django admin authentication methods
    "django.contrib.auth.backends.ModelBackend",
    # Allauth authentication methods
    "allauth.account.auth_backends.AuthenticationBackend",
]

SITE_ID = 1

ACCOUNT_AUTHENTICATION_METHOD = "username_email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "mandatory"
ACCOUNT_SIGNUP_EMAIL_ENTER_TWICE = True
ACCOUNT_USERNAME_MIN_LENGTH = 4
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = "/"

WSGI_APPLICATION = "shaping_surf.wsgi.application"


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

if "DATABASE_URL" in os.environ:
    DATABASES = {
        "default": dj_database_url.parse(os.environ.get("DATABASE_URL"))
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "UserAttributeSimilarityValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "MinimumLengthValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "CommonPasswordValidator"
        ),
    },
    {
        "NAME": (
            "django.contrib.auth.password_validation."
            "NumericPasswordValidator"
        ),
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"),)

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

if "DEV" in os.environ:
    STATICFILES_STORAGE = (
        "django.contrib.staticfiles.storage.StaticFilesStorage"
    )
else:
    STATICFILES_STORAGE = "whitenoise.storage.CompressedStaticFilesStorage"

# Base URL to generate newsletter unsubscribe links
if "DEV" in os.environ:
    BASE_URL = "http://127.0.0.1:8000"
else:
    BASE_URL = "https://shaping-sustainable-surf-8794b08a1b3a.herokuapp.com"

# Cloudinary settings
DEFAULT_FILE_STORAGE = "cloudinary_storage.storage.MediaCloudinaryStorage"
CLOUDINARY_URL = os.environ.get("CLOUDINARY_URL", "")

# Stripe settings
STRIPE_CURRENCY = "eur"
STRIPE_PUBLIC_KEY = os.getenv("STRIPE_PUBLIC_KEY", "")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY", "")

if "DEV" in os.environ:
    STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET_DEV", "")
else:
    STRIPE_WH_SECRET = os.getenv("STRIPE_WH_SECRET", "")

if "DEV" in os.environ:
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
    DEFAULT_FROM_EMAIL = "shapingsustainablesurf@gmail.com"
else:
    EMAIL_USE_TLS = True
    EMAIL_PORT = 587
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = os.getenv("EMAIL_HOST_USER", "")
    EMAIL_HOST_PASSWORD = os.getenv("EMAIL_HOST_PASS", "")
    DEFAULT_FROM_EMAIL = os.getenv("EMAIL_HOST_USER", "")

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
