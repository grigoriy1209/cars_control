from django.urls import path

from apps.payments.views import ExchangeRatesView

urlpatterns = [
    path('/exchange-rates', ExchangeRatesView.as_view(), name='exchange-rates'),
]
