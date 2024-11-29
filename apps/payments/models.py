from django.db import models
from django.utils import timezone

from core.models import BaseModel

from apps.payments.currency_choice import CurrencyChoice


class CurrencyModel(models.Model):
    class Meta:
        db_table = 'currency'

    currency = models.CharField(max_length=4, choices=CurrencyChoice.choices)
    course = models.DecimalField(decimal_places=4, max_digits=10)
    updated_at = models.DateTimeField(default=timezone.now, )

    def __str__(self):
        return f'{self.currency} - {self.course}'


class PriceModel(BaseModel):
    # car = models.ForeignKey(CarsModel, on_delete=models.CASCADE, related_name='prices')
    price = models.DecimalField(decimal_places=2, max_digits=10)
    currency = models.ForeignKey(CurrencyModel, on_delete=models.CASCADE, related_name='currency_prices')
    original_price = models.DecimalField(decimal_places=2, max_digits=10)
    currency_rate = models.ForeignKey(CurrencyModel, on_delete=models.SET_NULL, null=True, blank=True,
                                      related_name='course_prices')

    def __int__(self, *args, **kwargs):
        from apps.all_cars.listings.models import CarsModel
        self.car = models.ForeignKey(CarsModel, on_delete=models.CASCADE, related_name='prices')
        super().__int__(*args, **kwargs)

    def __str__(self):
        return f'{self.price} - {self.currency} - {self.currency_rate} - {self.car}'

    def save(self, *args, **kwargs):
        if self.currency:
            if self.currency.currency == 'USD':
                self.price = self.original_price * self.currency.course
            elif self.currency.currency == 'EUR':
                self.price = self.original_price * self.currency.course
            elif self.currency.currency == 'UAH':
                self.price = self.original_price
        super().save(*args, **kwargs)
