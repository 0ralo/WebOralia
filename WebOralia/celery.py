from celery import Celery
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WebOralia.settings')

app = Celery("WebOralia")

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


