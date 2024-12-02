from django.urls import include, path

from rest_framework import routers

from apps.all_cars.dropout_cars.views import BrandViewSet, ModelViewSet

router = routers.DefaultRouter()
router.register(r'brands', BrandViewSet, basename='brands')
router.register(r'models', ModelViewSet, basename='models')


urlpatterns = [
    path('', include(router.urls)),
]
