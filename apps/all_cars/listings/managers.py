from datetime import timedelta

from django.db import models
from django.db.models import Avg, Sum
from django.utils.timezone import now

from rest_framework.exceptions import PermissionDenied


class CarQuerySet(models.QuerySet):
    def filter_all_days(self, days):
        num_day = now() - timedelta(days=days)
        return self.filter(updated_at__gte=num_day)

    def views_count(self):
        return self.aggregate(total_views=Sum('views'))['total_views'] or 0

    def views_count_days(self, days):
        return self.filter_all_days(days).aggregate(total_views=Sum('views'))['total_views'] or 0

    def avg_price_region(self, region):
        return self.filter(region=region).aggregate(avg_price=Avg('price'))['avg_price']

    def avg_price_all_regions(self):
        return self.aggregate(avg_price=Avg('price'))['avg_price']


class CarManager(models.Manager):
    def get_queryset(self):
        return CarQuerySet(self.model)

    def views_count(self, user):
        if user.role_type != 'Premium_Seller':
            raise PermissionDenied("You are not allowed to view this car")
        return self.get_queryset().views_count()

    def views_count_days(self, user, days):
        if user.role_type != 'Premium_Seller':
            raise PermissionDenied("You are not allowed to view.")
        return self.get_queryset().views_count_days(days)

    def views_count_for_car(self, user, car_id):
        if user.role_type != 'Premium_Seller':
            raise PermissionDenied("You are not allowed to view.")
        car = self.get_queryset().filter(pk=car_id).first()
        if not car:
            raise PermissionDenied("No car with this id exists")
        return car.views

    def avg_price_region(self, user, region):
        if user.role_type != 'Premium_Seller':
            raise PermissionDenied('You are not allowed to view.')
        return self.get_queryset().avg_price_region(region)

    def avg_price_all_regions(self, user):
        if user.role_type != 'Premium_Seller':
            raise PermissionDenied('You are not allowed to view.')
        return self.get_queryset().avg_price_all_regions()
