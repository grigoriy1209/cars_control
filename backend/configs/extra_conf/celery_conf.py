CELERY_BROKER_URL = 'redis://redis:6379/0'
CELERY_RESULT_BACKEND = 'django-db'
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TIMEZONE = 'Europe/Kyiv'
CELERY_ENABLE_UTC = True

CELERY_BEAT_SCHEDULE = 'django_celery_beat.schedulers:DatabaseScheduler'
