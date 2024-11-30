from django.db import models


class EngineTypeChoice(models.TextChoices):
    INLINE = 'inline',
    V_TYPE = 'v-type',
    FLAT = 'flat',
    ROTARY = 'rotary',
    ELECTRIC = 'electric',
    HYBRID = 'hybrid',
    DIESEL = 'diesel',
    TURBOCHARGED = 'turbocharged',
    SUPERCHARGED = 'supercharged',
    W_TYPE = 'w-type',