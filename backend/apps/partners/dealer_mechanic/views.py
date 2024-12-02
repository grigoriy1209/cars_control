from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.partners.dealer_mechanic.models import DealerMechanicModel
from apps.partners.dealer_mechanic.serializers import DealerMechanicSerializer


class DealerMechanicViewSet(viewsets.ViewSet):
    queryset = DealerMechanicModel.objects.all()
    serializer_class = DealerMechanicSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
