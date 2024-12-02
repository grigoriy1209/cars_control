from django.utils.decorators import method_decorator

from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

from drf_yasg.utils import swagger_auto_schema

from core.pagination import PagePagination

from apps.all_cars.listings.filters import CarFilter
from apps.all_cars.listings.models import CarsModel
from apps.all_cars.listings.serializers import CarPhotoSerializer, CarSerializer
from apps.all_cars.listings.services import CarsService


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarListCreateView(ListCreateAPIView):
    """"
        get: list all cars
        post: create a new car
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    pagination_class = PagePagination
    filter_classes = (CarFilter,)
    queryset = CarsModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return (IsAuthenticated(),)

    def perform_create(self, serializer):
        # car = serializer.save(user=self.request.user,)
        # # description = serializer.validated_data.get('description')
        # brand = serializer.validated_data.get('brand')
        # car.update_status()
        if 'auto_saloon' in self.request.data:
            auto_saloon = self.request.data['auto_saloon']
            serializer.save(auto_saloon=auto_saloon)
        else:
            serializer.save(auto_saloon=None, user=self.request.user)
        serializer = self.get_serializer(data=serializer.data, context={'request': self.request})

    # def post(self, *args, **kwargs):
    #     data = self.request.data
    #     serializer = self.serializer_class(data=data, context={'request': self.request})
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_create(serializer)
    #     return Response(serializer.data, status=status.HTTP_201_CREATED)


@method_decorator(name='get', decorator=swagger_auto_schema(security=[]))
class CarListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    """
    get:list details of a car
    put:update details of a car
    patch:update details of a car
    delete:delete a car
    """
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return (IsAuthenticated(),)

    def get(self, *args, **kwargs):
        # car = get_object_or_404(CarsModel, pk=self.kwargs['pk'])
        car = self.get_object()
        CarsService.increment_view(car)
        serializer = self.get_serializer(car)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def perform_update(self, serializer):
        car = serializer.instance
        description = serializer.validated_data.get('description')
        car.description = description
        user = self.request.user
        car.update_status(user)
        serializer.save()


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
    """
    post: add photos to car
    """
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
