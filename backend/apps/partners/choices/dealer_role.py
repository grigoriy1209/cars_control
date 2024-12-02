from django.db import models


class DealerRoleType(models.TextChoices):
    DEALER_SELLER = 'Dealer_Seller'
    DEALER_MANAGER = 'Dealer_Manager'
    DEALER_ADMIN = 'Dealer_Admin'
    DEALER_MECHANIC = 'Dealer_Mechanic'
