from django.db import models


class UserRoleType(models.TextChoices):
    BUYER = 'Buyer'
    SELLER = 'Seller'
    PREMIUM_SELLER = 'Premium Seller'
    MANAGER = 'Manager'
    ADMIN = 'Admin'
    OWNER = 'Owner'


class AccountType(models.TextChoices):
    BASIC = 'Basic'
    PREMIUM = 'Premium'
