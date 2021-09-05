import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = "*"

INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "plausible",
    "tests",
    "django.contrib.admin",
    "django.contrib.contenttypes",
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
            ]
        },
    },
]

SECRET_KEY = "abcde12345"

ROOT_URLCONF = "tests.urls"
