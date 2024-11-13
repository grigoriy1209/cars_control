from datetime import timedelta

from django.db import models
from django.utils import timezone

from core.models import BaseModel


class AccountType(models.TextChoices):
    BASIC = 'Basic'
    PREMIUM = 'Premium'


class AccountModels(BaseModel):
    class Meta:
        db_table = 'accounts'

    user = models.OneToOneField('users.UserModel', on_delete=models.CASCADE, related_name='accounts')

    account_type = models.CharField(max_length=50, choices=AccountType.choices, default=AccountType.BASIC)

    start_date = models.DateField(auto_now_add=True)
    end_date = models.DateField(null=True, blank=True)
    active = models.BooleanField(default=True)

    def activate_premium_account(self, duration_days=30):
        self.account_type = AccountType.PREMIUM
        self.start_date = timezone.now().date()
        self.end_date = (timezone.now() + timedelta(days=duration_days)).date()
        self.active = True
        self.save()

    def is_premium_active(self):
        if self.account_type == AccountType.PREMIUM and self.end_date:
            return self.end_date > timezone.now().date() and self.active
        return False
