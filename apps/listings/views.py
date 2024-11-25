from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import (
    CreateAPIView,
    GenericAPIView,
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from core.pagination import PagePagination
from core.services.email_service import EmailService

from apps.all_users.auth.serializers import EmailSerializer
from apps.all_users.auth.views import UserModel
from apps.listings.filters import CarFilter
from apps.listings.models import CarsModel
from apps.listings.serializers import CarPhotoSerializer, CarSerializer
from apps.listings.services import CarsService


class CarListCreateView(GenericAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    pagination_class = PagePagination
    filter_classes = (CarFilter,)
    queryset = CarsModel.objects.all()

    def post(self, *args, **kwargs):
        data = self.request.data
        serializer = self.serializer_class(data=data,context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        car = serializer.save(user=self.request.user)
        user = get_object_or_404(UserModel, pk=self.request.user.id)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CarListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def put(self, request, *args, **kwargs):
        instance = self.get_object()

        CarsService.counter_edit_attempts(instance)
        return super().update(request, *args, **kwargs)


# class CarAddPhotoView(UpdateAPIView):
#     permission_classes = (IsAuthenticated,)
#     serializer_class = CarPhotoSerializer
#     queryset = CarsModel.objects.all()
#     http_method_names = ['put',]
#
#     def perform_update(self, serializer):
#         car = self.get_object()
#         car.photo.delete()
#         super().perform_update(serializer) #add 0ne photo


class CarAddPhotosView(CreateAPIView):
    permission_classes = [IsAuthenticated,]
    queryset = CarsModel.objects.all()

    def put(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        if car.photos.count() >=10:
            raise ValidationError('blblbl ')

        for index in files:
            serializer = CarPhotoSerializer(data={'photo': files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_201_CREATED)

