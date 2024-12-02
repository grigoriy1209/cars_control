from django.urls import include, path

from rest_framework import routers

from apps.partners.dealer_mechanic.views import DealerMechanicViewSet

router = routers.DefaultRouter()
router.register(r'dealer-mechanic', DealerMechanicViewSet, basename='dealer-mechanic')

urlpatterns = [
    path('', include(router.urls)),
]
