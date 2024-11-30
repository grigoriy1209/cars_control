from django.db import models


class EcologicalStandardTypeChoice(models.TextChoices):
    EVRO_6 = 'evro-6',
    EVRO_5 = "evro-5",
    EVRO_4 = "evro-4",
    EVRO_3 = "evro-3",
    EVRO_2 = "evro-2",
    EVRO_1 = "evro-1",
