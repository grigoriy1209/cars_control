from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from apps.listings.models import CarsModel
from apps.listings.serializers import CarSerializer


class CarListCreateView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CarSerializer
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
