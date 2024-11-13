from django.db.models.signals import post_save
from django.dispatch import receiver

from apps.all_users.accounts.models import AccountModels, AccountType
from apps.all_users.users.models import UserModel


@receiver(post_save, sender=UserModel)
def create_default_account(sender, instance, created, **kwargs):
    if created and not instance.account:
        account = AccountModels.objects.create(user=instance, account_type=AccountType.BASIC)
        instance.account = account
        instance.save(update_fields=['account'])
