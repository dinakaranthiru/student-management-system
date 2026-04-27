"""
settings.py - The CONFIGURATION FILE for your Django project.
This is like the "settings menu" of your app.
It tells Django things like:
  - Where is the database?
  - Which apps are installed?
  - What is the secret key?
"""

import os
from pathlib import Path  # Path helps us work with folder/file paths

# BASE_DIR = the root folder of your project
# Example: /home/yourname/student_management/
BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY - A unique password Django uses for security
# In real projects, NEVER share this key publicly!
SECRET_KEY = 'django-insecure-demo-key-for-learning-purposes-only-change-in-production'

# DEBUG = True means you'll see detailed error messages
# In real production apps, always set DEBUG = False
DEBUG = True

# ALLOWED_HOSTS - which domain names can access your app
# [] means only localhost (your own computer)
ALLOWED_HOSTS = ['*']

# INSTALLED_APPS - List of all "apps" in your Django project
# Django is made of small apps. Each app handles one thing.
INSTALLED_APPS = [
    'django.contrib.admin',        # The built-in Admin panel
    'django.contrib.auth',         # Login / logout system
    'django.contrib.contenttypes', # Helps different apps talk to each other
    'django.contrib.sessions',     # Remembers who is logged in
    'django.contrib.messages',     # Flash messages (success/error alerts)
    'django.contrib.staticfiles',  # CSS, images, JavaScript files
    'students',                    # OUR custom app (we will create this)
]

# MIDDLEWARE - Code that runs before/after every request
# Like security guards at the door
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',   # Prevents hacking attacks
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# ROOT_URLCONF - The main "map" of your website URLs
ROOT_URLCONF = 'student_management.urls'

# TEMPLATES - Where Django looks for HTML files
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Our HTML files go in a "templates" folder
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

# DATABASE - Where your data is stored
# SQLite = a simple file-based database, perfect for learning!
# The database file will be created as "db.sqlite3" in your project folder
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',  # Type of database
        'NAME': BASE_DIR / 'db.sqlite3',          # File location
    }
}

# STATIC FILES - CSS, JavaScript, Images
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key type for all models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Login redirect
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = 'login'
