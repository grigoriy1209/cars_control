from django.db import models


class ExchangeRates(models.Model):
    class Meta:
        db_table = 'exchange'

    currency = models.CharField(max_length=4, unique=True)
    rate = models.DecimalField(max_digits=10, decimal_places=2)
    updated_at = models.DateTimeField(auto_now=True)
