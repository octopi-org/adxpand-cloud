import os 
from .base import * 
# include this statment for out of the bos support with django
import django_heroku

DEBUG = os.environ.get('DEBUG', None)
if DEBUG is None:
    DEBUG = False
else:
    if 'true' == DEBUG.lower():
        DEBUG = True
    else:
        DEBUG = False

django_heroku.settings(locals())