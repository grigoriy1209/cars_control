from django.urls import path

from apps.all_cars.listings.views import CarAddPhotosView, CarListCreateView, CarListRetrieveUpdateDestroyView

urlpatterns = [
    path('', CarListCreateView.as_view(), name='car_list_create'),
    path('/<int:pk>', CarListRetrieveUpdateDestroyView.as_view(), name='car_list_retrieve_update_delete'),
    # path('/<int:pk>/photos', CarAddPhotoView.as_view(), name='car_add_photo'),
    path('/<int:pk>/photos', CarAddPhotosView.as_view(), name='car_add_photos'),
]
