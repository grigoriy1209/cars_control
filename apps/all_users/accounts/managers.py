from datetime import timedelta

from django.db import models
from django.utils import timezone

from apps.all_users.accounts.choices import AccountType


class AccountManager(models.Manager):

    def activate_premium_account(self, account,duration_days=30):
        self.account.account_type = AccountType.PREMIUM
        self.account.start_date = timezone.now().date()
        self.account.end_date = (timezone.now() + timedelta(days=duration_days)).date()
        self.account.active = True
        self.save()

    def is_premium_active(self):
        if self.account_type == AccountType.PREMIUM and self.end_date:
            return self.end_date > timezone.now().date() and self.active
        return False
