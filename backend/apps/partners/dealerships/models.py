from django.db import models

from core.models import BaseModel


class AutoSaloonModel(BaseModel):
    class Meta:
        db_table = 'AutoSaloons'

    name = models.CharField(max_length=20)
    description = models.TextField(max_length=500)
    address = models.TextField(max_length=100)

    user = models.ForeignKey('users.UserModel', on_delete=models.CASCADE, related_name='auto_saloons')

    def __str__(self):
        return self.name
