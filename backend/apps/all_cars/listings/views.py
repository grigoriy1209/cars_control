from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.pagination import PagePagination

from apps.all_cars.listings.filters import CarFilter
from apps.all_cars.listings.models import CarsModel
from apps.all_cars.listings.serializers import CarPhotoSerializer, CarSerializer
from apps.all_cars.listings.services import CarsService


class CarListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    pagination_class = PagePagination
    filter_classes = (CarFilter,)
    queryset = CarsModel.objects.all()

    def perform_create(self, serializer):
        # car = serializer.save(user=self.request.user,)
        # # description = serializer.validated_data.get('description')
        # brand = serializer.validated_data.get('brand')
        # car.update_status()
        serializer.save(user=self.request.user)

    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = self.serializer_class(data=data, context={'request': self.request})
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


class CarListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def get(self, *args, **kwargs):
        # car = get_object_or_404(CarsModel, pk=self.kwargs['pk'])
        car = self.get_object()
        CarsService.increment_view(car)
        serializer = self.get_serializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def perform_update(self, serializer):
    #     car = serializer.instance
    #     description = serializer.validated_data.get('description')
    #     car.description = description
    #     car.update_status()
    #     serializer.save()

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
    permission_classes = [IsAuthenticated, ]
    queryset = CarsModel.objects.all()

    def put(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        if car.photos.count() >= 10:
            raise ValidationError('Limit photo 10')

        for index in files:
            serializer = CarPhotoSerializer(data={'photo': files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_201_CREATED)
