from django.urls import include, path

from rest_framework import routers

from apps.dealerships.views import DealershipViewSet

router = routers.DefaultRouter()
router.register(r'dealers', DealershipViewSet, basename='dealers')
urlpatterns = [
    path('', include(router.urls)),
]
