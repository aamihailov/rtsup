# Django settings for rtsup project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('aamihailov', 'alexander.a.mihailov@gmail.com'),
    ('anastass', 'anastas.sanina@gmail.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'local_pg': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'study',                   
        'USER': 'techsup',                   
        'PASSWORD': '123123',                
        'HOST': 'localhost',
        'PORT': '',
        'OPTIONS': {
            'options': '-c search_path=techsup'
        }
    },
    'students51_pg': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'students51',                   
        'USER': 'pmm8101',                   
        'PASSWORD': 'retodarn',                
        'HOST': 'fpm2.ami.nstu.ru',
        'PORT': '',
        'OPTIONS': {
            'options': '-c search_path=_techsup_left'
        }
    },
    'students52_pg': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'students52',                   
        'USER': 'pmm8101',                   
        'PASSWORD': 'retodarn',                
        'HOST': 'fpm2.ami.nstu.ru',
        'PORT': '',
        'OPTIONS': {
            'options': '-c search_path=_techsup_right'
        }
    },
}
DATABASES['default'] = DATABASES['local_pg']
DATABASE_ROUTERS = ['rtsup.router.LeftRightRouter']

TIME_ZONE = 'Asia/Novosibirsk'

LANGUAGE_CODE = 'ru-ru'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'x-tmlnur!0r!28qhg9i$dvc^gqr6fdjaqttnrc#g%kxrb-13)b'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'rtsup.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'rtsup.wsgi.application'

TEMPLATE_DIRS = (
    '/home/aamihailov/Documents/Aptana Studio 3 Workspace/techsup/techsup_run/templates',
)

INSTALLED_APPS = (
    'left',
    'right',
    'django_extensions',
    'debug_toolbar'
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
