import os
from pathlib import Path
import environ



# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent



env=environ.Env()
environ.Env.read_env(os.path.join(BASE_DIR , ".env"))

#ENVİRON kısımlarını biz ekledik githuba secret_keyi göndermemek için  ************** AŞAĞISI ÖNEMLİİİİİİİİİİİİ

#NORMALDE environ.Env.read_env() BÖYLEYDİ AMA BİZ SETTINGS.PY DOSYASINI PARÇALADĞIMIZ İÇİN .env DOSYASINI 
#BULURKEN KAFASI KARIŞIYOR O YÜZDEN KENDİMİZ ELİMİZ İLE ONA BİR PATH VERİYORUZ Kİ .env DOSYASINA ULAŞABİLSİN


#DAHA SONRA LAUNCH.JSON DOSYASINA "--settings=config.settings.development" BU KODU YAZIYORUZ



#   NORMALDE YUKARIDAKİ PARENT SAYISI RESOLVEDEN SONRA 2 TANEYDİ AMA BİZ SETTİNGS.PY Yİ BİR KLASÖR DAHA 
#ALTA İNDİRDİĞİMİZ İÇİN BİR PARENT DAHA YAZDIK


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')




# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'account',
    'blog',
    #third party app
    'ckeditor',
    'crispy_forms',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

#templaterler için djangonun bakmasını istefiğimiz özel bir alan oluşturduk "DIRS":[BASE_DIR /'template'] diyerek sağladık bunu

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "template"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'




# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'tr'

#sistemin dilini türkçe yaptık ki bize türkçe mesajlar versin ekrana
#LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'


STATICFILES_DIRS=[
    BASE_DIR / "static"
]


AUTH_USER_MODEL="account.CustomUserModel"

MEDIA_URL="/media/"
MEDIA_ROOT=os.path.join(BASE_DIR,"media/")  

#base_dir demek manage.py dosyasının olduğu yol demek


CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = "/"



EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = '587'
DEFAULT_FROM_EMAIL = 'muhammetay651@gmail.com'
EMAIL_HOST_USER = 'muhammetay651@gmail.com'
EMAIL_HOST_PASSWORD = env("EMAIL_PASSWORD")





LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'basit_ifade': {
            'format': '{levelname} {asctime} {module}  {message}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
        'file': {
           
            'class': 'logging.FileHandler',
            'filename': 'logs/konu_okuma.log',
            'formatter': 'basit_ifade',
        }
    },
    'loggers': {
        'konu_okuma' : {

            'handlers': ['console', 'file'],
            'level': 'INFO',

        }
       
    },
}


