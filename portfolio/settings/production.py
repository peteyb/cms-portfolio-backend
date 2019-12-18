"""
production settings
"""

from urllib.parse import urlparse

import dj_database_url

# import raven

from .base import *  # noqa

ALLOWED_HOSTS = [
    'cms-portfolio-backend.herokuapp.com',
]

ENVIRONMENT = 'production'
SECRET_KEY = os.getenv('SECRET_KEY')
DEBUG = bool(os.getenv('DEBUG', False))
DATABASES['default'].update(dj_database_url.config(conn_max_age=500))
SECURE_SSL_REDIRECT = True

# redis_url = urlparse(os.getenv('REDISCLOUD_URL'))
# CACHES = {
#     'default': {
#         'BACKEND': 'redis_cache.RedisCache',
#         'LOCATION': '%s:%s' % (redis_url.hostname, redis_url.port),
#         'OPTIONS': {
#             'PASSWORD': redis_url.password,
#             'DB': 0,
#         }
#     }
# }
# CACHEOPS_REDIS = {
#     'host': redis_url.hostname,
#     'port': redis_url.port,
#     'password': redis_url.password,
#     'db': 0,
# }

# INSTALLED_APPS += ('raven.contrib.django.raven_compat',)

# RAVEN_CONFIG = {
#     'dsn': os.getenv('SENTRY_DSN')
# }

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['console'],
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s '
                      '%(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        # 'sentry': {
        #     'level': 'ERROR',
        #     'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        #     'tags': {'custom-tag': 'x'},
        # },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
        },
        # 'sentry.errors': {
        #     'level': 'DEBUG',
        #     'handlers': ['console'],
        #     'propagate': False,
        # },
        'django': {
            'handlers': ['console'],
            'level': os.getenv('DJANGO_LOG_LEVEL', 'ERROR'),
        },
    },
}

# CORS_ORIGIN_WHITELIST = (
#     'cms-portfolio-frontend.herokuapp.com',
# )

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = os.getenv('SENDGRID_USERNAME')
# EMAIL_HOST_PASSWORD = os.getenv('SENDGRID_PASSWORD')
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

# APP_URL = 'https://cms-portfolio-frontend.herokuapp.com'
