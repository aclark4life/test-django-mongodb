"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 5.1.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-d(&^zhd#n-px$jof8x9*1)pazi#40v8zr+y=yws(hhp!3nz1-^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "backend.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "backend.wsgi.application"


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
# test-django-mongodb
import os  # noqa
import dj_database_url  # noqa

INSTALLED_APPS.append("webpack_boilerplate")
INSTALLED_APPS.append("debug_toolbar")
PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)
STATICFILES_DIRS = []
STATICFILES_DIRS.append(os.path.join(BASE_DIR, "frontend/build"))
TEMPLATES[0]["DIRS"].append(os.path.join(PROJECT_DIR, "templates"))
WEBPACK_LOADER = {
    "MANIFEST_FILE": os.path.join(BASE_DIR, "frontend/build/manifest.json"),
}
DATABASES = {
    "default": {
        "ENGINE": "django_mongodb",
        "NAME": "test",
    }
}
DJANGO_COMPAT_CHECK_DISABLED = True
DEFAULT_AUTO_FIELD = "django_mongodb.fields.MongoAutoField"
MIGRATION_MODULES = {
    "admin": "backend.migrations.admin",
    "auth": "backend.migrations.auth",
    "contenttypes": "backend.migrations.contenttypes",
}
INSTALLED_APPS.remove("django.contrib.admin")
INSTALLED_APPS.remove("django.contrib.auth")
INSTALLED_APPS.remove("django.contrib.contenttypes")
INSTALLED_APPS.append("backend.apps.MongoAdminConfig")
INSTALLED_APPS.append("backend.apps.MongoAuthConfig")
INSTALLED_APPS.append("backend.apps.MongoContentTypesConfig")
INSTALLED_APPS.append("home")  # noqa