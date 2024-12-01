from django.core.cache import cache

from apps.payments.models import ExchangeRatesModel
from apps.payments.tasks import update_exchange_rates


class PaymentService:

    @staticmethod
    def get_currency_exchange_rates():
        exchange_rates = cache.get('exchange_rates')
        if not exchange_rates:
            exchange_rates = update_exchange_rates()
            cache.set('exchange_rates', exchange_rates, timeout=86400)
        return exchange_rates

    @staticmethod
    def update_currency_exchange_rates():
        rates = update_exchange_rates()
        ExchangeRatesModel.objects.create(**rates)
        return rates
