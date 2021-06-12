import os 
# include this statment for out of the box support with django
import django_heroku
from .base import * 

django_heroku.settings(locals())