from django.db import models


class CheckpointTypeChoice(models.TextChoices):
    MANUAL = 'manual',
    AUTOMATIC = 'automatic',
    TIPTRONIC = 'tiptronic',
    ROBOT = 'robot',
    VARIATOR = 'variator'
