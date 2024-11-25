from datetime import datetime, timedelta

from django.db import models

from rest_framework.exceptions import PermissionDenied

from apps.all_users.accounts.choices import AccountType
from apps.all_users.users.choices import UserRoleType


class CarQuerySet(models.QuerySet):
    def filter_all_views(self, views):
        return self.filter(views=views)

    def number_day_views(self, days=1):
        num_day = datetime.now() - timedelta(days=days)
        return self.filter(updated_at__gte=num_day)

    def number_week_views(self, days=7):
        num_day = datetime.now() - timedelta(days=days)
        return self.filter(updated_at__gte=num_day)

    def number_month_views(self, days=30):
        num_day = datetime.now() - timedelta(days=days)
        return self.filter(updated_at__gte=num_day)

    def avg_price_region(self, region):
        return self.filter(region=region).aggregate(avg_price=models.Avg('price'))['avg_price']

    def avg_price_all_regions(self):
        return self.aggregate(avg_price=models.Avg('price'))['avg_price']


class CarManager(models.Manager):
    def get_queryset(self):
        return CarQuerySet(self.model)

    def filter_all_views(self, user, views):
        self._premium_access(user)
        return self.get_queryset().filter_all_views(views)

    def number_day_views(self, days=1):

        return self.get_queryset().number_day_views(days)

    def number_week_views(self,days=7):

        return self.get_queryset().number_week_views(days)

    def number_month_views(self,days=30):

        return self.get_queryset().number_month_views(days)

    def avg_price_region(self,user, region):
        if user.role_type != 'Premium_Seller':
            raise PermissionDenied('bkblb')
        return self.get_queryset().avg_price_region(region)

    def avg_price_all_regions(self, user):
        if user.role_type != 'Premium_Seller':
            raise PermissionDenied('bkblb')
        return self.get_queryset().avg_price_all_regions()

# * кількість переглядів оголошення
# * кількість переглядів за день, тиждень, місяць
# * Середню ціну на авто по регіону продажу авто.
# * середня ціна авто по цілій Україні
