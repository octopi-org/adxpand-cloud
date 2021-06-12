import os 
from .base import * 
# include this statment for out of the bos support with django
import django_heroku

DEBUG = True

django_heroku.settings(locals())