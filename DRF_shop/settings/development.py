from DRF_shop.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('DATABASE-NAME', 'DRF_shop_db'),
        'USER': os.environ.get('DATABASE-USER', 'postgres'),
        'PASSWORD': os.environ.get('DATABASE-PASSWORD', 'postgres'),
        'HOST': os.environ.get('DATABASE-HOST', '127.0.0.1'),
        'PORT': os.environ.get('DATABASE-PORT', '5432'),
    }
}



STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')