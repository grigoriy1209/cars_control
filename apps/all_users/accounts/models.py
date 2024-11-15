from datetime import timedelta

from django.db import models
from django.utils import timezone

from core.models import BaseModel

from apps.all_users.accounts.choices import AccountType
from apps.all_users.accounts.managers import AccountManager


class AccountModels(BaseModel):
    class Meta:
        db_table = 'accounts'

    user = models.OneToOneField('users.UserModel', on_delete=models.CASCADE, related_name='accounts')

    account_type = models.CharField(max_length=50, choices=AccountType.choices, default=AccountType.BASIC)

    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    objects = AccountManager()

