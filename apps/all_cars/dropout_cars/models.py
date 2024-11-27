from django.db import models

from core.models import BaseModel


class BrandsModel(BaseModel):
    class Meta:
        db_table = 'cars_brands'
        ordering = ['id']

    title = models.CharField(max_length=25, unique=True)

    def __str__(self):
        return self.title


class ModelCar(BaseModel):
    class Meta:
        db_table = 'cars_models'
        ordering = ['id']

    model_car = models.CharField(max_length=25, )
    brand = models.ForeignKey(BrandsModel, on_delete=models.CASCADE, related_name='car_models')
