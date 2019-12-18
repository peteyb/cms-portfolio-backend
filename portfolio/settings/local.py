
"""
local settings
"""
import environ

from .base import *  # noqa

ENVIRONMENT = 'local'

LOCAL_ENV = environ.Env(
    SECRET_KEY=str,
    DEBUG=(bool, False),
    ALLOWED_HOSTS=(list, ['127.0.0.1:9200']),
    DATABASE_URL=str,
    REDIS_URL=str,
)
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))
SECRET_KEY = LOCAL_ENV('SECRET_KEY')
DEBUG = LOCAL_ENV('DEBUG')
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
