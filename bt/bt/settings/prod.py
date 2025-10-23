import os
from .base import *

SECRET_KEY = "django-insecure-vq)gqq*y-(u3!zv=3c21ko0mt6k73-kmy&m_y(xip6j4z&mj9-"
DEBUG = False
ALLOWED_HOSTS = ['.vercel.app']
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")