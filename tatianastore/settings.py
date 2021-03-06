# Django settings for tatianastore project.
import sys
import os
from decimal import Decimal

DEBUG = True
TEMPLATE_DEBUG = DEBUG


if "/srv/django" in os.getcwd():
    # Production server
    DEBUG = False
    PRODUCTION = True
else:
    # Development server
    DEBUG = True
    PRODUCTION = False

SITE_URL = "http://localhost:8000"
SITE_NAME = "Liberty Music Store"

PUBLIC_URL = "https://libertymusicstore.net"

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# Handle all uploads in memory
FILE_UPLOAD_MAX_MEMORY_SIZE = 8 * 1024 * 1024


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'tatianastore',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': 'localhost',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
        'ATOMIC_REQUESTS': True
    }
}

CACHES = {
    "default": {
        "BACKEND": "redis_cache.cache.RedisCache",
        "LOCATION": "127.0.0.1:6379:1",
        "OPTIONS": {
            "CLIENT_CLASS": "redis_cache.client.DefaultClient",
            'CONNECTION_POOL_KWARGS': {'max_connections': 10},
        }
    }
}


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = []

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'UTC'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = 'media'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'vh4p#9!k5vj#kr04u-mq=tn)7_3a%e_y35d!bzn41%v#6)0yoh'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'pagination_bootstrap.middleware.PaginationMiddleware',
    'django_requestlogging.middleware.LogSetupMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tatianastore.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'tatianastore.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.basename(__file__), "..", "templates"),
)

AUTH_USER_MODEL = 'tatianastore.User'

THUMBNAIL_ALIASES = {
    '': {
        'main_thumbnail': {'size': (96, 96), 'crop': True},
    },
}

THUMBNAIL_BASEDIR = 'thumbs'

THUMBNAIL_DEBUG = False

INSTALLED_APPS = (
    'sslserver',  # Facebook page tab development
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django_extensions',
    'django.contrib.admin',
    'django.contrib.humanize',
    "cryptoassets.django.app.CryptoassetsConfig",
    'registration',
    'crispy_forms',
    'captcha',
    'easy_thumbnails',
    'pagination_bootstrap',
    "djrill",
    'huey.djhuey',
    'tatianastore.app.TatianastoreConfig',
    'django_nose',
    'raven.contrib.django.raven_compat',
    'django_requestlogging',
    'andablog',
    'markitup',  # For entry content
    'taggit',  # For entry tags
)

SESSION_ENGINE = "django.contrib.sessions.backends.cache"

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },

        'request_format': {
            'format': '%(levelname)s %(asctime)s %(module)s %(remote_addr)s %(username)s %(request_method)s '
            '%(path_info)s %(server_protocol)s" %(http_user_agent)s '
            '%(message)s',
        },
    },

    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        },

       # Add an unbound RequestFilter.
       'request': {
           '()': 'django_requestlogging.logging_filters.RequestFilter',
       },
    },

    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },

        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
            'stream': sys.stdout
        },

        'rainbow': {
            "level": "DEBUG",
            "class": "rainbow_logging_handler.RainbowLoggingHandler",
            "stream": sys.stderr
        },

        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filters': ['request'],
            'filename': 'logs/django.log',
            'formatter': 'request_format',
        },

        'sentry': {
            'level': 'WARN',
            'class': PRODUCTION and 'raven.contrib.django.raven_compat.handlers.SentryHandler' or 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },

        'django.db.backends': {
            'handlers': [],
            'level': 'ERROR',
            'propagate': True,
        },

        'sqlalchemy': {
            'level': 'ERROR',
            'propagate': False,
        },

        'py.warnings': {
            'level': 'ERROR',
            'propagate': False,
        },

        '': {
            'level': PRODUCTION and 'WARN' or 'DEBUG',
            'handlers': [PRODUCTION and 'sentry' or 'rainbow', 'file'],
        },

    }
}

if "cryptoassets_helper_service" in sys.argv:
    LOGGING["loggers"][""]["level"] = "INFO"

CRISPY_TEMPLATE_PACK = 'bootstrap3'

#: Don't make the users log in unnecessarily
SESSION_COOKIE_AGE = 365 * 24 * 3600

THUMBNAIL_ALIASES = {
    '': {
        'main': {'size': (1024, 768), 'crop': False},
        'thumbnail': {'size': (127, 128), 'crop': False},
    },
}

ACCOUNT_ACTIVATION_DAYS = 3

#: How many BTCs short we can be for transactions to make sure they are confirmed
TRANSACTION_BALANCE_CONFIRMATION_THRESHOLD_BTC = Decimal("0.00001")

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

SOUTH_MIGRATION_MODULES = {
    'easy_thumbnails': 'easy_thumbnails.south_migrations',
}

# Disable some warning pollution
import warnings
warnings.filterwarnings('ignore', r"DateTimeField received a naive datetime", RuntimeWarning, r'django\.db\.models\.fields')

# Add this to your settings.py
if DEBUG:
    # Install rainbow logging handler when running Django in develoment mode
    import sys
    LOGGING["handlers"]["rainbow"] = {"level": "DEBUG", "class": "rainbow_logging_handler.RainbowLoggingHandler", 'stream': sys.stderr}
    LOGGING["loggers"]['']["handlers"].append("rainbow")


HUEY = {
    'backend': 'huey.backends.redis_backend',  # required.
    'name': 'Huey Redis',
    'connection': {'host': 'localhost', 'port': 6379},
    'always_eager': False, # Defaults to False when running via manage.py run_huey
    'consumer_options': {'workers': 3},
}

LOGIN_REDIRECT_URL = "/admin/"


TEMPLATE_CONTEXT_PROCESSORS = ("django.contrib.auth.context_processors.auth",
"django.core.context_processors.debug",
"django.core.context_processors.i18n",
"django.core.context_processors.media",
"django.core.context_processors.static",
"django.core.context_processors.tz",
"django.contrib.messages.context_processors.messages",
"tatianastore.contextprocessors.extra_vars"
)

#: Override this value to make unguessable wallet hook URLs
BLOCKCHAIN_WEBHOOK_SECRET = ""

# Only run actual Bitcoin payments to the artist if the site URLs matches these
# (to avoid sending payments out accidentally)
ALLOWED_CREDIT_SITE_URLS = ["https://libertymusicstore.net"]

CURRENCIES = [
    ("USD", "USD"),
    ("EUR", "EUR"),
    ("GBP", "GBP"),
]

COIN_NAME ="Bitcoin"

ASK_CURRENCY = True

PAYMENT_CURRENCY = "btc"

PAYMENT_SOURCE = "cryptoassets"

CURRENCY_SYMBOL = "BTC"

DEFAULT_PAYMENT_CURRENCY_NAME = "USD"

DEFAULT_PRICING_CURRENCY = "USD"

DEFAULT_ALBUM_PRICE = Decimal("10.0")

DEFAULT_SONG_PRICE = Decimal("0.90")

# How much we spend in unit tests for doing the actual payment (testnet bitcoins)
TEST_CREDITING_PRICE = Decimal("0.50")  # in USG

# TESTNET settings
CRYPTOASSETS = {

    # You can use a separate database for cryptoassets,
    # or share the Django database. In any case, cryptoassets
    # will use a separate db connection.
    "database": {
        "url": "postgresql://localhost/cryptoassets_testnet",
        "echo": False,
    },

    "coins": {
        # Locally running bitcoind in testnet
        "btc": {
            "backend": {
                "class": "cryptoassets.core.backend.blockio.BlockIo",
                "api_key": "923f-e3e9-a580-dfb2",
                "network": "btctest",
                "pin": "foobar123",
                # Cryptoassets helper process will use this UNIX named pipe to communicate
                # with bitcoind
                "walletnotify": {
                    "class": "cryptoassets.core.backend.sochainwalletnotify.SochainWalletNotifyHandler",
                    "pusher_app_key": "e9f5cc20074501ca7395"
                },
            }
        },
    },

    # Bind cryptoassets.core event handler to Django dispacth wrapper
    "events": {
        "django": {
            "class": "cryptoassets.core.event.python.InProcessEventHandler",
            "callback": "cryptoassets.django.incoming.handle_tx_update"
        }
    },

    "status_server": {
        "ip": "127.0.0.1",
        "port": 9001
    }
}

MARKITUP_FILTER = ('markdown.markdown', {'safe_mode': False})
MARKITUP_SET = 'markitup/sets/markdown'


from tatianastore.local_settings import *

