"""
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def abspath(*args):
    return os.path.abspath(os.path.join(*args))


ADMIN_NAME = "Admin"
ADMIN_EMAIL = "admin@foo.bar"
ADMIN_FROM_EMAIL = "{} <{}>".format(ADMIN_NAME, ADMIN_EMAIL)
DEFAULT_FROM_EMAIL = "Biostar Mailer <admin@foo.bar>"

SERVER_EMAIL = "Server Email <{}>".format(ADMIN_EMAIL)

ADMINS = [
    (ADMIN_NAME, ADMIN_EMAIL),
]

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv(
    "SECRET_KEY") or 'x6-76b$bvosk=u1p#xe#qo@(ib_(15how%lawko4-!^&qruzo%'

# SECURITY WARNING: don't run with debug turned on in production!
if os.getenv("BIOSTAR_DEPLOY"):
    DEBUG = False
else:
    DEBUG = True

ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost www.lvh.me 127.0.0.1").split()

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',
    'taggit',
    'biostar4.forum.apps.Biostar4',
]

MIDDLEWARE_CLASSES = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'biostar4.middleware.BiostarMiddleware',
]

ROOT_URLCONF = 'biostar4.urls'

if os.getenv("THEME_DIRS"):
    template_dirs = os.getenv("THEME_DIRS").split()
else:
    template_dirs = []

# Search the theme directories first.
TMPL_DIRS = template_dirs + [
    abspath(BASE_DIR, "forum", "templates")
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': TMPL_DIRS,
        'APP_DIRS': True,

        'OPTIONS': {
            'string_if_invalid': '*** MISSING VARIABLE ***',
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'biostar4.wsgi.application'

TAGGIT_CASE_INSENSITIVE = True

# The database is used only to 'pacify' addons
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'www', 'db', 'biostar4.sqlite3'),
    }
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# The google ID will be injected as a template variable.
GOOGLE_TRACKER = ""
GOOGLE_DOMAIN = ""

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

if os.getenv("STATICFILES_DIRS"):
    static_dirs = os.getenv("STATICFILES_DIRS").split()
else:
    static_dirs = []

STATICFILES_DIRS = static_dirs + [
    os.path.join(BASE_DIR, "forum", "static"),
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}

WHOOSH_INDEX = abspath(BASE_DIR, 'www', 'whoosh')

STATIC_ROOT = os.getenv("STATIC_ROOT") or os.path.join(BASE_DIR, "www", "export", "static")
MEDIA_ROOT = os.getenv("MEDIA_ROOT") or os.path.join(BASE_DIR, "www", "export", "media")

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'

# Google RECAPTHCA settings.
RECAPTCHA_ENABLED = bool(os.getenv("RECAPTCHA_ENABLED"))
RECAPTCHA_SITE_KEY = os.getenv("RECAPTCHA_SECRET_KEY", "")
RECAPTCHA_SECRET_KEY = os.getenv("RECAPTCHA_SECRET_KEY", "")

# Mongodb settings.
MONGODB_NAME = os.getenv("MONGODB_NAME", "biostar-test")
MONGODB_URI = os.getenv("MONGODB_URI", "mongodb://localhost:27017/")

# Email settings
EMAIL_BACKEND = os.getenv(
    "EMAIL_BACKEND") or 'django.core.mail.backends.console.EmailBackend'
