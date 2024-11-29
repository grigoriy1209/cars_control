from datetime import datetime

from django.core import validators as V
from django.db import models

from rest_framework.exceptions import ValidationError

from core.models import BaseModel
from core.services.email_service import EmailService

from apps.all_users.users.models import UserModel

from ...payments.models import PriceModel
from ..dropout_cars.models import BrandsModel, ModelCar
from .choices.body_type_choice import BodyTypeChoice
from .choices.eco_choice import EcologicalStandardTypeChoice
from .choices.engine_choice import EngineTypeChoice
from .choices.status_choice import StatusChoice
from .choices.transmission_choice import CheckpointTypeChoice
# from .currency_choice import CurrencyChoice
from .managers import CarManager
from .regex import CarRegex
from .services import CarsService


class CarsModel(BaseModel):
    class Meta:
        db_table = 'cars'
        ordering = ('id',)

    # brand = models.CharField(max_length=15, validators=[V.RegexValidator(*CarRegex.BRAND.value)])
    # model = models.CharField(max_length=15, validators=[V.RegexValidator(*CarRegex.MODEL.value)])
    brand = models.ForeignKey(BrandsModel, on_delete=models.CASCADE, related_name='cars', null=False, blank=False)
    model = models.ForeignKey(ModelCar, on_delete=models.CASCADE, related_name='cars')
    year = models.IntegerField(validators=[V.MinValueValidator(1950), V.MaxValueValidator(datetime.now().year)])
    # price = models.IntegerField(validators=[V.MinValueValidator(0), V.MaxValueValidator(1_000_000)])
    # currency = models.CharField(max_length=15, choices=CurrencyChoice.choices)
    price = models.ForeignKey(PriceModel,on_delete=models.SET_NULL, related_name='cars', null=True, blank=True)
    mileage = models.IntegerField(validators=[V.MinValueValidator(10), V.MaxValueValidator(1_000_000)])
    body_type = models.CharField(max_length=25, choices=BodyTypeChoice.choices)
    engine = models.CharField(max_length=25, choices=EngineTypeChoice.choices)
    eco_standard = models.CharField(max_length=25, choices=EcologicalStandardTypeChoice.choices)
    checkpoint = models.CharField(max_length=25, choices=CheckpointTypeChoice.choices)
    color = models.CharField(max_length=23, validators=[V.MinLengthValidator(2)])
    status = models.CharField(max_length=20, choices=StatusChoice.choices, default=StatusChoice.PENDING)
    region = models.CharField(max_length=23, validators=[V.RegexValidator(*CarRegex.REGION.value)])
    description = models.TextField(max_length=500, validators=[V.MinLengthValidator(2)], null=False, blank=False)
    # photo = models.ImageField(upload_to=upload_car_photos, blank=True)
    edit_attempts = models.PositiveIntegerField(default=0)

    views = models.PositiveIntegerField(default=0)

    user = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='cars')

    objects = CarManager()

    foul_words = ['fuck', 'Fucking']

    def validate_foul(self):
        description_lower = self.description.lower()
        return any(word in description_lower for word in self.foul_words)

    def update_status(self,user):
        if self.validate_foul():
            self.edit_attempts += 1

            if self.edit_attempts >= 3:
                self.status = StatusChoice.INACTIVE
                EmailService.notify_manager(user)
        else:
            self.status = StatusChoice.ACTIVE
            self.edit_attempts = 0
        self.save()

    def count_views(self):
        self.views += 1
        self.save()

    def get_price(self):
        if self.price:
            return self.price.price
        return self.price if self.price is not None else 0


class CarPhotoModel(BaseModel):
    class Meta:
        db_table = 'car_photos'

    photo = models.ImageField(upload_to=CarsService.upload_car_photos, blank=True)
    car = models.ForeignKey(CarsModel, on_delete=models.CASCADE, related_name='photos')

    def save(self, *args, **kwargs):
        if self.car.photos.count() >= 10:
            raise ValidationError("too many photos")
        super().save(*args, **kwargs)
