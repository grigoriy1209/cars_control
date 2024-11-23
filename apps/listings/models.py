from datetime import datetime

from django.core import validators as V
from django.db import models

from core.models import BaseModel

from apps.all_users.users.models import UserModel

from .choices.body_type_choice import BodyTypeChoice
from .choices.currency_choice import CurrencyChoice
from .choices.eco_choice import EcologicalStandardTypeChoice
from .choices.engine_choice import EngineTypeChoice
from .choices.transmission_choice import CheckpointTypeChoice
from .managers import CarManager
from .regex import CarRegex
from .services import CarsService


class CarsModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    brand = models.CharField(max_length=15, validators=[V.RegexValidator(*CarRegex.BRAND.value)])
    model = models.CharField(max_length=15, validators=[V.RegexValidator(*CarRegex.MODEL.value)])
    year = models.IntegerField(validators=[V.MinValueValidator(1950), V.MaxValueValidator(datetime.now().year)])
    price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1_000_000)])
    mileage = models.IntegerField(validators=[V.MinValueValidator(10), V.MaxValueValidator(1_000_000)])
    currency = models.CharField(max_length=15, choices=CurrencyChoice.choices)
    body_type = models.CharField(max_length=25, choices=BodyTypeChoice.choices)
    engine = models.CharField(max_length=25, choices=EngineTypeChoice.choices)
    eco_standard = models.CharField(max_length=25, choices=EcologicalStandardTypeChoice.choices)
    checkpoint = models.CharField(max_length=25, choices=CheckpointTypeChoice.choices)
    color = models.CharField(max_length=23, validators=[V.MinLengthValidator(2)])
    is_active = models.BooleanField(default=True)
    # status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.PENDING)
    region = models.CharField(max_length=23, validators=[V.RegexValidator(*CarRegex.REGION.value)])
    description = models.TextField(max_length=500, validators=[V.MinLengthValidator(2)],null=False)
    # photo = models.ImageField(upload_to=upload_car_photos, blank=True)
    edit_attempts = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()

    def validate_foul(self):
        return CarsService.validate_foul(self.description)


class CarPhotoModel(BaseModel):
    class Meta:
        db_table = 'car_photos'

    photo = models.ImageField(upload_to=CarsService.upload_car_photos, blank=True)
    car = models.ForeignKey(CarsModel, on_delete=models.CASCADE, related_name='photos')
