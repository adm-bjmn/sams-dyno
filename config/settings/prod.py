
from .base import *
from decouple import config

SECRET_KEY = config('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = []


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]
# STATIC_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(os.path.dirname(BASE_DIR), 'media/')


# Email Settings
# Prod
'''
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'adm.bjmn@gmail.com'
EMAIL_HOST_PASSWORD = 'env'
EMAIL_USE_TLS = True
# EMAIL_USEW_SSL = False


myaccount.goog.com/lesssecureapps
myaccount.goog.com/DisplayUnlockCaptcha
turn on.

OR // 

turn on two factor auth.
myaccount.google.com/apppasswords


Always Check ports - google django send gmail.
'''
