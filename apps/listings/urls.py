from django.urls import path

from apps.listings.views import CarListCreateView, CarListRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarListRetrieveUpdateDestroyView.as_view(), name='car_list_retrieve_update_delete'),
]
