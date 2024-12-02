from django.urls import path

from .views import (
    AvgPriceRegionApiView,
    AvgPriceRegionsView,
    ViewsByDaysApiView,
    ViewsCountApiView,
    ViewsCountForCarsApiView,
)

urlpatterns = [
    path('/views/count', ViewsCountApiView.as_view(), name='count_views'),
    path('/views/count/days/<int:days>', ViewsByDaysApiView.as_view(), name='count_views_by_days'),
    path('/views/car/<int:car_id>', ViewsCountForCarsApiView.as_view(), name='count_views_by_car'),
    path('/avg_price/region/<str:region>', AvgPriceRegionApiView.as_view(), name='avg_price_region'),
    path('/avg_price/all-regions', AvgPriceRegionsView.as_view(), name='avg_price_all_regions'),
]
