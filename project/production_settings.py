DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'contest',
        'USER': 'develop',
        'PASSWORD': 'qwerty12+',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
STATIC_URL = 'http://belzik.webfactional.com/static/'
STATIC_ROOT = '/home/belzik/webapps/static'
STATICFILES_DIRS = ('/home/belzik/webapps/static',)

STATICFILES_FINDERS = ('django.contrib.staticfiles.finders.FileSystemFinder', 'django.contrib.staticfiles.finders.AppDirectoriesFinder',)