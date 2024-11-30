from datetime import timedelta

from django.db import models
from django.utils import timezone

from apps.all_users.accounts.choices import AccountType


class AccountManager(models.Manager):

    def activate_premium_account(self, account, duration_days=30):
        account.account_type = AccountType.PREMIUM
        account.start_date = timezone.now().date()
        account.end_date = (timezone.now() + timedelta(days=duration_days)).date()
        account.active = True
        account.save()
        return account

    def is_premium_active(self,account):
        if account.account_type == AccountType.PREMIUM and account.end_date:
            return account.end_date > timezone.now().date() and account.active
        return False
