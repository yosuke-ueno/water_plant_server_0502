import os
from pathlib import Path

#settings.pyからそのままコピー
BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-wna$933lf2gi7h6wjj)tpxtp9*t4+_0990nz+%j-aiud#*+m9k'

#settings.pyからそのままコピー
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

DEBUG = False #ローカルでDebugできるようになります