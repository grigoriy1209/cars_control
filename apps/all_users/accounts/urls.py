from django.urls import path

from apps.all_users.accounts.views import PremiumToBasicAccountView, UserToPremiumAccountView

urlpatterns = [
    path('/<int:pk>/user_to_premium', UserToPremiumAccountView.as_view(), name='user_to_premium'),
    path('/<int:pk>/premium_to_basic', PremiumToBasicAccountView.as_view(), name='premium_to_basic'),
]
