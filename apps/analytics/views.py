from rest_framework.response import Response
from rest_framework.views import APIView

from core.permissions.is_superuser_permission import IsStaff

from apps.all_cars.listings.models import CarsModel
from apps.all_users.users.permissions import IsPremiumSeller


class ViewsCountApiView(APIView):
    permission_classes = (IsStaff,)

    def get(self, request, *args, **kwargs):
        user = request.user
        total_views = CarsModel.objects.views_count(user=user)
        return Response({'total_views': total_views, })


class ViewsByDaysApiView(APIView):
    permission_classes = (IsPremiumSeller,)

    def get(self, request, *args, **kwargs):
        user = request.user
        days = int(kwargs.get('days', 10))
        if days <= 0:
            return Response({'error': 'days must be greater than zero'}, status=400)
        try:
            views = CarsModel.objects.views_count_days(user=user, days=days)
        except Exception as e:
            return Response({'error': str(e)}, status=400)
        return Response({'views': views, 'days': days})


class ViewsCountForCarsApiView(APIView):
    permission_classes = (IsPremiumSeller,)

    def get(self, request, *args, **kwargs):
        user = request.user

        car_id = kwargs.get('car_id')
        CarsModel.objects.get(pk=car_id)
        views = CarsModel.objects.views_count_for_car(car_id=car_id, user=user)
        return Response({'views': views, 'car_id': car_id})


class AvgPriceRegionApiView(APIView):
    permission_classes = [IsPremiumSeller]

    def get(self, request, *args, **kwargs):
        user = request.user
        region = kwargs.get('region', None)

        avg_price = CarsModel.objects.avg_price_region(user=user, region=region)
        return Response({'avg_price': avg_price, 'region': region})


class AvgPriceRegionsView(APIView):
    permission_classes = [IsPremiumSeller, ]

    def get(self, request, *args, **kwargs):
        user = request.user
        avg_price = CarsModel.objects.avg_price_all_regions(user=user, )
        return Response({'avg_price_all_regions': avg_price})
