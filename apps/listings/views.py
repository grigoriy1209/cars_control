from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from better_profanity import profanity

from core.pagination import PagePagination

from apps.listings.filters import CarFilter
from apps.listings.models import CarsModel
from apps.listings.serializers import CarPhotoSerializer, CarSerializer


class CarListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    pagination_class = PagePagination
    filter_classes = (CarFilter,)
    queryset = CarsModel.objects.all()

    def post(self, request, *args, **kwargs):
        user = request.user

        data = request.data.copy()
        data['user'] = user.id

        serializer = self.get_serializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CarListRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
    queryset = CarsModel.objects.all()

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.edit_attempts += 1
        instance.save()
        if instance.edit_attempts > 3:
            CarsModel.objects.filter(id=instance.id).update(status='inactive')
            raise ValidationError({"detail": "You have reached the maximum number of edit attempts"})
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
    pagination_class = [IsAuthenticated,]
    queryset = CarsModel.objects.all()

    def put(self, *args, **kwargs):
        files = self.request.FILES
        car = self.get_object()
        for index in files:
            serializer = CarPhotoSerializer(data={'photo':files[index]})
            serializer.is_valid(raise_exception=True)
            serializer.save(car=car)
        car_serializer = CarSerializer(car)
        return Response(car_serializer.data, status=status.HTTP_201_CREATED)

