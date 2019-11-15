"""
Django settings for elsa project.

Generated by 'django-admin startproject' using Django 1.11.1.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""






# @AtmosStudent  
#     This is the settings.py page for the ELSA project.  This page lists settings for the following:
#         1. hosts                            6. middleware
#         2. directories                      7. root url conf (k Might be causing probs w allowedhosts)
#         3. security                         8. templates
#         4. performance                      9. WSGI Application
#         5. application definition          10. database(s) (k Unsure if plural is true)
#     This page lists settings for many more properties or components of a web application.  The most
#     important property is security.  Make sure you check out the security section.  It isn't necessary
#     to understand it fully, but before you mess with this particular document, you probably should
#     refrain from changing any of the security sections until you are ready to do so... But with the
#     exception of one security section.  It's the one section that doesn't work for local but does work
#     in production.  Check out SSL redirect.  It (k for me at least) is the easiest security feature
#     to learn about.



import os
from datetime import date
# --------------------------------
from secrets import *

for_production = allowed_hosts_production()
for_local = allowed_hosts_local()

# --------------------------------

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ARCHIVE_DIR = os.path.join(BASE_DIR, 'archive')
LOG_DIR = os.path.join(BASE_DIR, 'logs')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
TEMPORARY_DIR = os.path.join(BASE_DIR, 'temporary')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/
#     Please read the document listed above.  As you read it, please ensure to go through this file and 
#     double, triple, quadruple check that it satisfies the above document.  If it doesn't, fix it.
#     As of January 2017, some things are not satisfied that should be.  Help a sista out! -k






# ---SECURITY SECTION-----------------------------
# 




#     SECURITY WARNING: keep the secret key used in production secret!  
#     This needs to be moved out of this file!
SECRET_KEY = secret_key()









#     SECURITY WARNING: don't run with debug turned on in production!
#                   use live debug for quick checks in production.
DEBUG = True





#    The following is literally read, if the DEBUG variable is set to False, then the only allowed hosts are those listed for production only.  By allowing DEBUG to be True AND using only the allowed hosts for production, we open ourselves up to vulnerabilities from outside attackers.
if DEBUG == False:
    ALLOWED_HOSTS = for_production
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    X_FRAME_OPTIONS = 'DENY'

    #     SECURITY WARNING: Set this to True to avoid transmitting the CSRF cookie over HTTP accidentally
    CSRF_COOKIE_SECURE = True     # Keep Commented Out in Development

    #     SECURITY_WARNING: Set this to True to avoid transmitting the session cookie over HTTP accidentally
    SESSION_COOKIE_SECURE = True     # Keep Commented Out in Development


else:
    ALLOWED_HOSTS = for_local
    #dirpath = os.getcwd()
    #print 'Current working directory for settings.py: {}'.format(dirpath)





# ---END SECURITY SECTION-----------------------------


# ---PERFORMANCE SECTION-----------------------------
# ---END PERFORMANCE SECTION-----------------------------





# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'build',
    'friends',
    'main',
    'review',
    'tutorial',
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

ROOT_URLCONF = 'elsa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATE_DIR,],
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

WSGI_APPLICATION = 'elsa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Chihuahua'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [STATIC_DIR, ]

# User files (User directories, Bundle directories, ...)
# https://atmos.nmsu.edu/elsa/student_lair/   NEED TO ADD POST AND FIX THIS

ARCHIVE_URL = '/archive/'
ARCHIVEFILES_DIRS = [ARCHIVE_DIR, ]

# User uploaded files (documents, data files)
MEDIA_URL = ARCHIVE_URL

# Logger
# https://docs.djangoproject.com/en/2.0/topics/logging/

#LOGGING = {
#    'version': 1,
#    'disable_existing_loggers': False,
#    'handlers': {
#        'file': {
#            'level': 'DEBUG',
#            'class': 'logging.FileHandler',
#            'filename': '/logs/first_test.txt',
#        },
#    },
#    'loggers': {
#        'django': {
#            'handlers':['file'],
#            'level': 'DEBUG',
#            'propogate': True,
#        },
#    },
#}



