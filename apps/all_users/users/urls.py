from django.urls import path

from apps.all_users.users.views import MeInfoView, UserListCreateView, UserRetrieveUpdateDestroyView

urlpatterns = [
    path('', UserListCreateView.as_view(), name='user_list_create'),
    path('/<int:pk>/update_to_user', UserRetrieveUpdateDestroyView.as_view(), name='user_retrieve_update_delete'),
    path('/me_info', MeInfoView.as_view(), name='user_me_info'),
]
