from django.db import models


class UserRoleType(models.TextChoices):
    BUYER = 'Buyer'
    SELLER = 'Seller'
    MANAGER = 'Manager'
    ADMIN = 'Admin'


class AccountType(models.TextChoices):
    BASIC = 'Basic'
    PREMIUM = 'Premium'
