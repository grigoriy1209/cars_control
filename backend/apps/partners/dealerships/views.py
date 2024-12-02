from django.shortcuts import get_object_or_404

from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from core.pagination import PagePagination

from apps.all_cars.listings.models import CarsModel
from apps.all_cars.listings.serializers import CarSerializer
from apps.partners.dealerships.models import AutoSaloonModel
from apps.partners.dealerships.serializers import AutoSaloonSerializer
from apps.partners.permishions.dealer_permishions import IsDealerAdmin


class DealershipViewSet(viewsets.ViewSet):
    queryset = AutoSaloonModel.objects.all()
    serializer_class = AutoSaloonSerializer
    pagination_class = PagePagination
    permission_classes = (IsDealerAdmin,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AutoSaloonAddCarViewSet(viewsets.ModelViewSet):
    serializer_class = CarSerializer

    def get_queryset(self):
        auto_saloon_id = self.kwargs['auto_saloon_pk']
        auto_saloon = get_object_or_404(AutoSaloonModel, pk=auto_saloon_id)
        return CarsModel.objects.filter(auto_saloon=auto_saloon)

    def create(self, request, *args, **kwargs):
        # auto_saloon_id = kwargs.get('auto_saloon_pk')
        # try:
        #     auto_saloon = AutoSaloonModel.objects.get(id=auto_saloon_id)
        # except AutoSaloonModel.DoesNotExist:
        #     raise Http404("Auto salon not found")
        auto_saloon_id = kwargs.get('auto_saloon_pk')
        auto_saloon = get_object_or_404(AutoSaloonModel, pk=auto_saloon_id)

        serializer = CarSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(auto_saloon=auto_saloon)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


# class AutoSaloonAddUserViewSet(viewsets.ModelViewSet):
#     serializer_class = UserSerializer
#
#     def get_queryset(self):
#         user_id = self.kwargs['user_id']
#         user = get_object_or_404(UserModel, pk=user_id)
#         return AutoSaloonModel.objects.filter(user=user)
#
#     def create(self, request, *args, **kwargs):
#         user_id = self.kwargs['user_id']
#         user = get_object_or_404(UserModel, pk=user_id)
#
#         serializer = UserSerializer(data=request.data, )
#         serializer.is_valid(raise_exception=True)
#         serializer.save(user=user)
#         auto_saloon = AutoSaloonModel.objects.create(user=user, **request.data)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
