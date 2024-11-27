from rest_framework import viewsets

from apps.all_cars.dropout_cars.models import BrandsModel, ModelCar
from apps.all_cars.dropout_cars.serializers import BrandSerializer, ModelSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)


class ModelViewSet(viewsets.ModelViewSet):
    queryset = ModelCar.objects.all()
    serializer_class = ModelSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)



