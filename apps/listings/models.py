from django.db import models

from core.models import BaseModel

from apps.all_users.users.models import UserModel
from apps.listings.choices import (
    BodyTypeChoice,
    CheckpointTypeChoice,
    CurrencyChoice,
    EcologicalStandardTypeChoice,
    EngineTypeChoice,
    StatusChoice,
)


class CarsModel(BaseModel):
    class Meta:
        db_table = 'cars'

    brand = models.CharField(max_length=15)
    model = models.CharField(max_length=15)
    year = models.IntegerField()
    price = models.IntegerField()
    mileage = models.IntegerField()
    currency = models.CharField(max_length=15, choices=CurrencyChoice.choices)
    body_type = models.CharField(max_length=25, choices=BodyTypeChoice.choices)
    engine = models.CharField(max_length=25, choices=EngineTypeChoice.choices)
    eco_standard = models.CharField(max_length=25, choices=EcologicalStandardTypeChoice.choices)
    checkpoint = models.CharField(max_length=25, choices=CheckpointTypeChoice.choices)
    color = models.CharField(max_length=23)
    status = models.CharField(max_length=20, choices=StatusChoice.choices)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')

    def save(self, *args, **kwargs):
        if self.user.account == 'Basic' and self.user.cars.count() >= 1:
            raise ValueError("basic account allows you to place only one ad.")
        super().save(*args, **kwargs)
