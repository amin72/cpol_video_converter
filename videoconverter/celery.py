import os
from celery import Celery
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videoconverter.settings')
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('videoconverter_celery_app')

app.conf.broker_url = BASE_REDIS_URL
app.conf.result_backend = BASE_REDIS_URL

app.autodiscover_tasks(settings.INSTALLED_APPS)
