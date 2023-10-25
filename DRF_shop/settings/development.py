from DRF_shop.settings.base import *

LOCAL_APPS = [
    'apps.product.apps.ProductConfig',
    'apps.media.apps.MediaConfig',
]

THIRD_PARTY_APPS = [
    'rest_framework',
    'treebeard',
    'drf_spectacular',

]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    *THIRD_PARTY_APPS,
    *LOCAL_APPS
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE-NAME', 'DRF_shop_db'),
        'USER': os.environ.get('DATABASE-USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE-PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE-HOST', 'localhost'),
        'PORT': os.environ.get('DATABASE-PORT', '5432'),
    }
}

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = 'medias/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'medias')