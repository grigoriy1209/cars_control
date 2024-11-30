from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models

from core.models import BaseModel

from apps.all_users.accounts.models import AccountModels
from apps.all_users.users.choices import UserRoleType
from apps.all_users.users.managers import UserManager


class UserModel(AbstractBaseUser, BaseModel, PermissionsMixin):
    class Meta:
        db_table = 'auth_user'

    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    role_type = models.CharField(max_length=20,
                                 choices=UserRoleType.choices, default=UserRoleType.SELLER)
    account = models.OneToOneField('accounts.AccountModels', on_delete=models.CASCADE, related_name='users',
                                   null=True, blank=True)
    # account_type = models.CharField(max_length=20, choices=AccountType.choices, default=AccountType.BASIC.value)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = UserManager()


class ProfileModel(BaseModel):
    class Meta:
        db_table = 'profile'

    name = models.CharField(max_length=25)
    surname = models.CharField(max_length=25)
    age = models.IntegerField()
    phone = models.CharField(max_length=20)
    user = models.OneToOneField(UserModel, on_delete=models.CASCADE, related_name='profile')
