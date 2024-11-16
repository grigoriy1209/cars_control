from django.db import models

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response

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
from apps.listings.managers import CarManager


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
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.PENDING)
    region = models.CharField(max_length=23)
    edit_count = models.PositiveIntegerField(default=0)
    edit_attempts = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()

