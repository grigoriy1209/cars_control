from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.partners.dealer_admin.models import DealerAdminModel
from apps.partners.dealer_admin.serializers import DealerAdminSerializer


class DealerAdminViewSet(viewsets.ViewSet):
    queryset = DealerAdminModel.objects.all()
    serializer_class = DealerAdminSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
