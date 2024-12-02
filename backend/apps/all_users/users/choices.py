from django.db import models


class UserRoleType(models.TextChoices):
    BUYER = 'Buyer'
    SELLER = 'Seller'
    PREMIUM_SELLER = 'Premium_Seller'
    MANAGER = 'Manager'
    ADMIN = 'Admin'
    OWNER = 'Owner'

    # dealers
    # DEALER_SELLER = 'Dealer_Seller'
    # DEALER_MANAGER = 'Dealer_Manager'
    # DEALER_ADMIN = 'Dealer_Admin'
    # DEALER_MECHANIC = 'Dealer_Mechanic'
