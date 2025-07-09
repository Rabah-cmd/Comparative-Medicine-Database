web: gunicorn comparative_medicine_database.wsgi:application --bind 0.0.0.0:$PORT
release: python manage.py migrate

import os

# Heroku: Update database configuration from $DATABASE_URL
import dj_database_url
if 'DATABASE_URL' in os.environ:
    DATABASES['default'] = dj_database_url.config(
        conn_max_age=500,
        conn_health_checks=True,
    )

# Static files (CSS, JavaScript, Images)
MIDDLEWARE.insert(1, 'whitenoise.middleware.WhiteNoiseMiddleware')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Allow all host headers (required for Heroku)
if 'DYNO' in os.environ:
    ALLOWED_HOSTS = ['*']
