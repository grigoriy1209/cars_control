from django.urls import include, path

from rest_framework.routers import DefaultRouter

from rest_framework_nested.routers import NestedDefaultRouter

from apps.dealerships.views import AutoSaloonAddCarViewSet, DealershipViewSet

router = DefaultRouter()
router.register(r'dealers', DealershipViewSet, basename='dealers')

nested_router = NestedDefaultRouter(router, r'dealers', lookup='auto_saloon')
nested_router.register(r'cars', AutoSaloonAddCarViewSet, basename='dealer-cars')
urlpatterns = [
    path('', include(router.urls)),
    path('', include(nested_router.urls)),
]
