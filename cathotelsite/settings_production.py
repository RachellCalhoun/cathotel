from .settings import *

DEBUG = False
ALLOWED_HOSTS = ['udadak.pythonanywhere.com']

SECRET_KEY = os.environ.get('SECRET_KEY', None)
