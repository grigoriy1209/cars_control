from django.urls import path

from apps.all_users.admins.views import AdminToUserView, UserBanView, UserToAdminView, UserUnbanView

urlpatterns = [
    path('/<int:pk>/ban', UserBanView.as_view(), name='user_ban'),
    path('/<int:pk>/unban', UserUnbanView.as_view(), name='user_unban'),
    path('/<int:pk>/to_admin', UserToAdminView.as_view(), name='user_to_admin'),
    path('/<int:pk>/admin_to_user', AdminToUserView.as_view(), name='admin_to_user'),

]