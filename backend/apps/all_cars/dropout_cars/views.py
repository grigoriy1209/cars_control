from django.http import Http404
from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.response import Response

from core.services.email_service import EmailService

from apps.all_cars.dropout_cars.models import BrandsModel, ModelCar
from apps.all_cars.dropout_cars.serializers import BrandSerializer, ModelSerializer


class BrandViewSet(viewsets.ModelViewSet):
    queryset = BrandsModel.objects.all()
    serializer_class = BrandSerializer

    lookup_field = 'title'

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        title = kwargs.get('title')
        try:
            brand = get_object_or_404(BrandsModel, title=title)
        except Http404:
            EmailService.notify_admin_error_brand()
            return Response({'error': "not brand"}, status.HTTP_404_NOT_FOUND)

        serializer = self.get_serializer(brand)
        return Response(serializer.data, status.HTTP_200_OK)


class ModelViewSet(viewsets.ModelViewSet):
    queryset = ModelCar.objects.all()
    serializer_class = ModelSerializer
    lookup_field = 'model_car'

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    def create(self, *args, **kwargs):
        return super().create(*args, **kwargs)

    def retrieve(self, *args, **kwargs):
        model_car = kwargs.get('model_car')
        try:
            model_car = get_object_or_404(ModelCar, model_car=model_car)
        except Http404:
            EmailService.notify_admin_error_brand()
            return Response({'error': "not model_car"}, status.HTTP_404_NOT_FOUND)
        serializer = self.get_serializer(model_car)
        return Response(serializer.data, status.HTTP_200_OK)
