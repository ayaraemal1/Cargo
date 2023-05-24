# Caching
# https://docs.djangoproject.com/en/4.0/topics/cache/

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
    },
}

# Django Sessions
SESSION_ENGINE = "django.contrib.sessions.backends.cached_db"
