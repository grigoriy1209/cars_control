from django.urls import path

from apps.all_users.accounts.views import UserToPremiumAccountView

urlpatterns = [
    path('/<int:pk>/user_to_premium', UserToPremiumAccountView.as_view(), name='user_to_premium'),
]
