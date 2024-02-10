"""
Django settings for school_management_system project.

Generated by 'django-admin startproject' using Django 4.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-vejv_l41#brfz!7%)g7z#d2ri9d7^mdkbwtin0u2g+%+=@s1d^"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "school-management-system-alpha.vercel.app",
    "school-management-system-git-main-ademics-projects.vercel.app",
]
# ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "corsheaders",
    "debug_toolbar",
    "django_filters",
    "drf_yasg",
    "djoser",
    "users",
    "core",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]

ROOT_URLCONF = "school_management_system.urls"

AUTH_USER_MODEL = "users.CustomUser"

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework.authentication.TokenAuthentication",
    ),
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"],
}

DJOSER = {
    "LOGIN_FIELD": "email",
    "SEND_ACTIVATION_EMAIL": True,
    "USER_CREATE_PASSWORD_RETYPE": True,
    "USERNAME_CHANGED_EMAIL_CONFIRMATION": True,
    "PASSWORD_CHANGED_EMAIL_CONFIRMATION": True,
    "SEND_CONFIRMATION_EMAIL": True,
    "PASSWORD_RESET_CONFIRM_URL": "reset_password/{uid}/{token}",
    "USERNAME_RESET_CONFIRM_URL": "reset_email_confirm/{uid}/{token}",
    "ACTIVATION_URL": "activation/{uid}/{token}",
    "EMAIL": {
        "activation": "users.email.CustomActivationEmail",
        "confirmation": "users.email.CustomConfirmationEmail",
        "password_reset": "users.email.CustomPasswordResetEmail",
        "password_changed_confirmation": "users.email.CustomPasswordConfirmationEmail",
        "username_changed_confirmation": "users.email.UsernameChangedConfirmationEmail",
        "username_reset": "users.email.UsernameResetEmail",
    },
    "SERIALIZERS": {
        "user_create": "users.serializers.UserCreateSerializer",
        "user": "users.serializers.UserSerializer",
    },
}


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
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

WSGI_APPLICATION = "school_management_system.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": config("DATABASE_ENGINE", default="django.db.backends.sqlite3"),
        "NAME": config("DATABASE_NAME", default="db.sqlite3"),
        "USER": config("DATABASE_USER", default="myuser"),
        "PASSWORD": config("DATABASE_PASSWORD", default="mypassword"),
        "HOST": config("DATABASE_HOST", default="localhost"),
        "PORT": config("DATABASE_PORT", default=""),
    }
}
# Email configurations
EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)
EMAIL_HOST = config("EMAIL_HOST", default="smtp.gmail.com")
EMAIL_PORT = config("EMAIL_PORT", default=587, cast=int)
EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="example@gmail.com")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="your_password")
EMAIL_USE_TLS = config("EMAIL_USE_TLS", default=True, cast=bool)
DEFAULT_FROM_EMAIL = "THE GEM TEAM"
# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")

# Media settings
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")


INTERNAL_IPS = [
    "127.0.0.1",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://school-management-system-ui.vercel.app",
]
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
