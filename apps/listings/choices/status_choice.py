from django.db import models


class StatusChoice(models.TextChoices):
    ACTIVE = 'active',
    INACTIVE = 'inactive',
    PENDING = 'pending',

