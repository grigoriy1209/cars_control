from rest_framework import status, viewsets
from rest_framework.response import Response

from apps.partners.dealer_manager.models import DealerManager
from apps.partners.dealer_manager.serializers import DealerManagerSerializer
from apps.partners.dealer_seller.models import DealerSellerModel
from apps.partners.dealer_seller.serializers import DealerSellerSerializer


class DealerSellerViewSet(viewsets.ViewSet):
    queryset = DealerSellerModel.objects.all()
    serializer_class = DealerSellerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status.HTTP_201_CREATED)
