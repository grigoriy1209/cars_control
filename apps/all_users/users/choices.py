from django.db import models


class UserRoleType(models.TextChoices):
    BUYER = 'Buyer'
    SELLER = 'Seller'
    PREMIUM_SELLER = 'Premium_Seller'
    MANAGER = 'Manager'
    ADMIN = 'Admin'
    OWNER = 'Owner'


