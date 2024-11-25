from django.urls import path

from apps.analytics.views import AvgPriceRegionApiView, AvgPriceRegionsView, NumberViewApiView

urlpatterns = [
    path('/views/<int:days>', NumberViewApiView.as_view(), name='number_views'),
    path('/avg_price/region/<str:region>', AvgPriceRegionApiView.as_view(), name='avg_price_region'),
    path('/avg_price/all-regions', AvgPriceRegionsView.as_view(), name='avg_price_all_regions'),
]
