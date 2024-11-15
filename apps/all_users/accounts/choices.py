from django.db import models


class AccountType(models.TextChoices):
    BASIC = 'Basic'
    PREMIUM = 'Premium'
