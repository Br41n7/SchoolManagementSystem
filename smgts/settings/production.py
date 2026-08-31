import os
from .base import *

DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-production-key-change-me")

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "*").split(",")

RENDER_EXTERNAL_HOSTNAME = os.getenv("RENDER_EXTERNAL_HOSTNAME")
if RENDER_EXTERNAL_HOSTNAME:
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

try:
    from .local import *
except ImportError:
    pass
