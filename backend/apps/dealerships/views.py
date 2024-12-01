from rest_framework import viewsets

from apps.dealerships.models import AutoSaloonModel
from apps.dealerships.serializers import AutoSaloonSerializer


class DealershipViewSet(viewsets.ModelViewSet):
    queryset = AutoSaloonModel.objects.all()
    serializer_class = AutoSaloonSerializer
