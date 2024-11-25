from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.all_cars.listings.models import CarsModel
from apps.all_users.users.permissions import IsPremiumSeller

from configs.settings import ALLOWED_HOSTS


class NumberViewApiView(APIView):
    permission_classes = [IsPremiumSeller,]

    def get(self, request, *args, **kwargs):
        user = request.user
        days = int(kwargs.get('days', 1))

        view_count = CarsModel.objects.number_day_views(user=user, days=days)
        return Response(view_count)


class AvgPriceRegionApiView(APIView):
    permission_classes = [IsPremiumSeller]

    def get(self, request, *args, **kwargs):
        user = request.user
        region = kwargs.get('region', None)

        avg_price = CarsModel.objects.avg_price_region(user=user, region=region)
        return Response({'avg_price': avg_price, 'region': region})


class AvgPriceRegionsView(APIView):
    permission_classes = [IsPremiumSeller,]

    def get(self, request, *args, **kwargs):
        user = request.user
        avg_price = CarsModel.objects.avg_price_all_regions(user=user,)
        return Response(avg_price)
