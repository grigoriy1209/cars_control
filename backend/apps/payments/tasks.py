from decimal import Decimal

from django.core.cache import cache

import requests
from celery import shared_task

from apps.payments.models import ExchangeRatesModel


@shared_task
def update_exchange_rates():
    url = "https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    rates = {}
    for rate in data:
        if rate['ccy'] == 'USD':
            rates["USD_UAH"] = Decimal(rate['sale'])
        elif rate['ccy'] == 'EUR':
            rates["EUR_UAH"] = Decimal(rate['sale'])
    if "USD_UAH" in rates and "EUR_UAH" in rates:
        rates["USD_EUR"] = rates["USD_UAH"] / rates["EUR_UAH"]

    cache.set('exchange_rates', rates, timeout=86400)

    ExchangeRatesModel.objects.create(
        usd_to_uah=rates["USD_UAH"],
        eur_to_uah=rates["EUR_UAH"],
        usd_to_eur=rates["USD_EUR"],
    )
    return rates
