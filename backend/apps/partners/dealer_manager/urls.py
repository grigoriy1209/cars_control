from django.urls import include, path

from rest_framework import routers

from apps.partners.dealer_manager.views import DealerManagerViewSet

router = routers.DefaultRouter()
router.register(r'dealer-manager', DealerManagerViewSet, basename='dealer-manager')

urlpatterns = [
    path('', include(router.urls)),
]
