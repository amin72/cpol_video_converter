import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'videoconverter.settings')
BASE_REDIS_URL = os.environ.get('REDIS_URL', 'redis://localhost:6379')

app = Celery('videoconverter_celery_app')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.broker_url = BASE_REDIS_URL
app.conf.result_backend = BASE_REDIS_URL
