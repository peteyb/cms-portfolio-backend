
"""
local settings
"""
import environ
import cloudinary

from .base import *  # noqa

ENVIRONMENT = 'local'

LOCAL_ENV = environ.Env(
    SECRET_KEY=str,
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ['127.0.0.1:9200']),
    DATABASE_URL=str,
    REDIS_URL=str,
    BUILD_HOOK_URL=str,
    CLOUDINARY_NAME=str,
    CLOUDINARY_KEY=str,
    CLOUDINARY_SECRET=str,
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = LOCAL_ENV('SECRET_KEY')
DEBUG = LOCAL_ENV('DEBUG')
BUILD_HOOK_URL = LOCAL_ENV('BUILD_HOOK_URL')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'portfolio',
        'USER': 'portfolio',
        'PASSWORD': 'portfolio',
        'HOST': 'db',
        'PORT': 5432,
    }
}

# cloudinary image config
cloudinary.config(
    cloud_name=LOCAL_ENV('CLOUDINARY_NAME'),
    api_key=LOCAL_ENV('CLOUDINARY_KEY'),
    api_secret=LOCAL_ENV('CLOUDINARY_SECRET'),
)

# CACHES = {
#     "default": {
#         "BACKEND": "redis_cache.RedisCache",
#         "LOCATION": "redis://redis:6379",
#         "OPTIONS": {
#             "PASSWORD": SECRET_KEY,
#             "DB": 0,
#         }
#     }
# }
# CACHEOPS_REDIS = "redis://redis:6379/1"

# debugging
ALLOWED_HOSTS = ['localhost', 'portfolio.dev.local']
# INSTALLED_APPS.append('debug_toolbar')
# MIDDLEWARE.append('debug_toolbar.middleware.DebugToolbarMiddleware')
INTERNAL_IPS = ('172.30.0.1')


# CORS_ORIGIN_WHITELIST = (
#     'localhost:4200'
# )

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
