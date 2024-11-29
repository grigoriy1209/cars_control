from django.db import models


class CurrencyChoice(models.TextChoices):
    USD = 'USD',
    EUR = 'EUR',
    UAH = 'UAH',
