"""
This file contains all the settings that defines the development server.

SECURITY WARNING: don't run with debug turned on in production!
"""

import logging
from typing import List

from core.settings.components.common import DATABASES, INSTALLED_APPS, MIDDLEWARE

# Setting the development status:

DEBUG = True

ALLOWED_HOSTS = [
    "*",
]


# Installed apps for development only:

INSTALLED_APPS += (
    # Better debug:
    "nplusone.ext.django",
    # Linting migrations:
    "django_migration_linter",
    # django-test-migrations:
    "django_test_migrations.contrib.django_checks.AutoNames",
    # This check might be useful in production as well,
    # so it might be a good idea to move `django-test-migrations`
    # to prod dependencies and use this check in the main `settings.py`.
    # This will check that your database is configured properly,
    # when you run `python manage.py check` before deploy.
    "django_test_migrations.contrib.django_checks.DatabaseConfiguration",
    # django-extra-checks:
    "extra_checks",
)


# Static files:
# https://docs.djangoproject.com/en/4.0/ref/settings/#std:setting-STATICFILES_DIRS

STATICFILES_DIRS: List[str] = ["static"]


# nplusone
# https://github.com/jmcarp/nplusone

# Should be the first in line:
MIDDLEWARE = ("nplusone.ext.django.NPlusOneMiddleware",) + MIDDLEWARE  # noqa: WPS440

# Logging N+1 requests:
# NPLUSONE_RAISE = True  # comment out if you want to allow N+1 requests
NPLUSONE_LOGGER = logging.getLogger("django")
NPLUSONE_LOG_LEVEL = logging.WARN
NPLUSONE_WHITELIST = [
    {"model": "admin.*"},
]

# django-extra-checks
# https://github.com/kalekseev/django-extra-checks

EXTRA_CHECKS = {
    "checks": [
        # Forbid `unique_together`:
        "no-unique-together",
        # Require non empty `upload_to` argument:
        "field-file-upload-to",
        # Use the indexes option instead:
        "no-index-together",
        # Each model must be registered in admin:
        "model-admin",
        # FileField/ImageField must have non-empty `upload_to` argument:
        "field-file-upload-to",
        # Don't pass `null=False` to model fields (this is django default)
        "field-null",
        # ForeignKey fields must specify db_index explicitly if used in
        # other indexes:
        {"id": "field-foreign-key-db-index", "when": "indexes"},
        # If field nullable `(null=True)`,
        # then default=None argument is redundant and should be removed:
        "field-default-null",
        # Fields with choices must have companion CheckConstraint
        # to enforce choices on database level
        "field-choices-constraint",
        # DRF:
        "drf-model-serializer-extra-kwargs",
    ],
}

# Disable persistent DB connections
# https://docs.djangoproject.com/en/4.0/ref/databases/#caveats
DATABASES["default"]["CONN_MAX_AGE"] = 0
