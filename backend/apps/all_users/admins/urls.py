from django.urls import path

from .views import ManagerToUserView, UserBanView, UserToManagerView, UserUnbanView

urlpatterns = [
    path('/<int:pk>/ban', UserBanView.as_view(), name='user_ban'),
    path('/<int:pk>/unban', UserUnbanView.as_view(), name='user_unban'),
    path('/<int:pk>/to_manager', UserToManagerView.as_view(), name='user_to_manager'),
    path('/<int:pk>/manager_to_user', ManagerToUserView.as_view(), name='manager_to_user'),

]