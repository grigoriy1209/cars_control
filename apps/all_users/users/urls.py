from django.urls import path

from apps.all_users.users.signals import TestEmailView
from apps.all_users.users.views import MeInfoView, UserCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', UserCreateView.as_view(), name='user_create'),
    path('/<int:pk>', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_delete'),
    path('/me_info', MeInfoView.as_view(), name='user_me_info'),
    path('/test', TestEmailView.as_view(), name='test_email'),
]
