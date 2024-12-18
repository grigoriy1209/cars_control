import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'configs.settings')
app = Celery('settings')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'send_spam_every_minutes': {
        'task': 'core.services.email_service.spam',
        'schedule': crontab(),

    },
    'update-exchange-rates-every-day': {
        'task': 'payments.tasks.update_exchange_rates',
        'schedule': crontab(minute='0', hour='09',),
    }

}
app.conf.timezone = 'UTC'
