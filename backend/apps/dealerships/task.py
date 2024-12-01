from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from apps.dealerships.models import AutoSaloonModel


def create_custom_permissions():
    content_type = ContentType.objects.get_for_model(AutoSaloonModel)
    permissions = [
        ('can_create_car', 'Can create car'),
        ('can_update_car', 'Can update car'),
        ('can_delete_car', 'Can delete car'),
        ('can_view_car', 'Can view car'),
    ]
    for codename, name in permissions:
        Permission.objects.create(
            name=name,
            content_type=content_type
        )
