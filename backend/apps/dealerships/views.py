from django.http import Http404

from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.all_cars.listings.models import CarsModel
from apps.all_cars.listings.serializers import CarSerializer
from apps.dealerships.models import AutoSaloonModel
from apps.dealerships.serializers import AutoSaloonSerializer


class DealershipViewSet(viewsets.ViewSet):
    queryset = AutoSaloonModel.objects.all()
    serializer_class = AutoSaloonSerializer


class AutoSaloonAddCarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def create(self, request, *args, **kwargs):
        auto_saloon_id = kwargs.get('auto_saloon_pk')
        try:
            auto_saloon = AutoSaloonModel.objects.get(id=auto_saloon_id)
        except AutoSaloonModel.DoesNotExist:
            raise Http404("Auto salon not found")

        serializer = CarSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_saloon=auto_saloon)

        return Response(serializer.data, status=status.HTTP_201_CREATED)
