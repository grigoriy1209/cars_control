from django.urls import include, path

from rest_framework import routers

from apps.partners.dealer_seller.views import DealerSellerViewSet

router = routers.DefaultRouter()
router.register(r'dealer-seller', DealerSellerViewSet, basename='dealer-seller')

urlpatterns = [
    path('', include(router.urls)),
]
