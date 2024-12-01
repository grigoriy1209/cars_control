from django.db import models


class ExchangeRatesModel(models.Model):
    class Meta:
        db_table = 'exchange'

    usd_to_uah = models.DecimalField(max_digits=12, decimal_places=4)
    eur_to_uah = models.DecimalField(max_digits=12, decimal_places=4)
    usd_to_eur = models.DecimalField(max_digits=12, decimal_places=4)
    updated_at = models.DateTimeField(auto_now=True)

    @classmethod
    def get_latest_rates(cls):
        return cls.objects.last()

    def __str__(self):
        return f'{self.usd_to_eur}: {self.usd_to_uah} {self.eur_to_uah}'

