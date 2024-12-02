from django.db import models

from core.models import BaseModel

from apps.partners.choices.dealer_role import DealerRoleType


class DealerManager(BaseModel):
    class Meta:
        db_table = 'dealer_manager'

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    age = models.IntegerField()
    role = models.CharField(max_length=50,choices=DealerRoleType.choices,default=DealerRoleType.DEALER_MANAGER)
