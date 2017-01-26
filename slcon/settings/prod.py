# production-environment specific settings
import os

from .base import *

DEBUG = False

ALLOWED_HOSTS = ['*']

SECRET_KEY = os.getenv('SECRET_KEY', None)
