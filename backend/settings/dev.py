# test-django-mongodb
from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

try:
    from .local import *  # noqa
except ImportError:
    pass

LOG_LEVEL = os.environ.get("LOG_LEVEL", "DEBUG")
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {"console": {"class": "logging.StreamHandler"}},
    "root": {"handlers": ["console"], "level": "WARNING"},
}
INTERNAL_IPS = [
    "127.0.0.1",
]
INSTALLED_APPS.append("django.contrib.admindocs")  # noqa
MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware")  # noqa
SECRET_KEY = "mhZYefgCBgoM0ye8vLIQq9aTP/HRo2I3yNkMaCNQwU2hOZgRSGnawtQG0wS6s+ga"
