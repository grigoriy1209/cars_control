from django.urls import include, path

from rest_framework import routers

from apps.partners.dealer_admin.views import DealerAdminViewSet

router = routers.DefaultRouter()
router.register(r'dealer-admin', DealerAdminViewSet, basename='dealer-admin')

urlpatterns = [
    path('', include(router.urls)),
]
