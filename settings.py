from pathlib import Path
import os
import dj_database_url

# Base Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Media Files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Static Files
STATIC_URL = '/static/'
#STATIC_ROOT = BASE_DIR / 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
# Security
SECRET_KEY = os.getenv('SECRET_KEY', 'your-fallback-secret-key')  # Use env variable for production
DEBUG = os.getenv('DEBUG', 'True') == 'True'  # Toggle debug mode using environment variable
#ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1:8000').split(',')  # Set hosts via env variable
#ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1:8000').split(',')
# Installed Apps
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'corsheaders',
    'products',
]

# Custom User Model
AUTH_USER_MODEL = 'products.User'
DATABASES = {
    'default': dj_database_url.config(
        # Replace this value with your local database's connection string.
        default='postgresql://datachristo_user:bWX59EXP2MhlOG0yMyQZ1vrqmJsIfeKt@dpg-d0dn922dbo4c738o67m0-a/datachristo',
        conn_max_age=600
    )
}



# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# CORS Policy
CORS_ALLOWED_ORIGINS = os.getenv('CORS_ALLOWED_ORIGINS', 'http://localhost:3000').split(',')
CORS_ALLOWED_ORIGIN_REGEXES = os.getenv('CORS_ALLOWED_ORIGIN_REGEXES', '').split(',')
CORS_ALLOW_ALL_ORIGINS=True
# URLs
ROOT_URLCONF = 'shop_backend.urls'

# Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

# WSGI
WSGI_APPLICATION = 'shop_backend.wsgi.application'

# Database Configuration
DATABASES = {
     'default': dj_database_url.config(default=f'sqlite:///{BASE_DIR / "db.sqlite3"}')
}

# Password Validators
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
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Default Primary Key Field
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# API Key
SELAR_API_KEY = os.getenv('SELAR_API_KEY', 'sat_3iv9q393aw97c7m211140770p2l')  # Set default for development
#ALLOWED_HOSTS = ['https://christoper-fashion-backend.onrender.com']
ALLOWED_HOSTS = [
    'christoper-fashion-backend.onrender.com',  # Your deployed domain
    'localhost',  # For local testing
]
