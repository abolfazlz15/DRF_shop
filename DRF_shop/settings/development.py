from DRF_shop.settings.base import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'DRF_shop_db', 
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': '127.0.0.1', 
        'PORT': '5432',
    }
}
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')