from settings import *

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'l$$_2h*(es(s0nju_bjy$tluwfsy2642v$8vtu5(!u8j078d3!'

TEMPLATE_DEBUG = DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'tehpug',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': 5432
    }
}

MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + (
    'querycount.middleware.QueryCountMiddleware',
    'devserver.middleware.DevServerMiddleware'
)

INSTALLED_APPS = INSTALLED_APPS + (
    'devserver',
    'debug_toolbar',
    'django_extensions'
)

QUERYCOUNT_THRESHOLDS = {
    'MEDIUM': 50,
    'HIGH': 200,
    'MIN_TIME_TO_LOG': 0,
    'MIN_QUERY_COUNT_TO_LOG': 0
}

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
)

ADMINS = (('Keyvan Hedayati', 'k1.hedayati93@gmail.com'),)
