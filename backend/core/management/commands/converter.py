from django.core.management import BaseCommand

from rest_framework import status

import requests

from apps.payments.models import ExchangeRatesModel


class Command(BaseCommand):
    def handle(self, *args, **options):
        try:
            response = requests.get('https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5')
            if response.status_code != status.HTTP_200_OK:
                self.stdout.write(self.style.ERROR(response.json()))

            data = response.json()

            if not data:
                self.stdout.write(self.style.SUCCESS(response.json()))
                return

            for item in data:
                currency_code = item['ccy']
                exchange_rate = item['sale']  # курс продажі

                if currency_code == 'USD':
                    currency, created = ExchangeRatesModel.objects.get_or_create(currency='USD')
                    currency.course = exchange_rate  # update course
                    currency.save()
                    self.stdout.write(self.style.SUCCESS('Successfully converted currency to USD'))

                elif currency_code == 'EUR':
                    currency, created = ExchangeRatesModel.objects.get_or_create(currency='EUR')
                    currency.course = exchange_rate
                    currency.save()
                    self.stdout.write(self.style.SUCCESS('Successfully converted currency to EUR'))
                elif currency_code == 'UAH':
                    currency, created = ExchangeRatesModel.objects.get_or_create(currency='UAH')
                    currency.course = 1
                    currency.save()
                    self.stdout.write(self.style.SUCCESS('Successfully converted currency to UAH'))
            else:
                self.stdout.write(self.style.SUCCESS('No currencies found'))

        except requests.exceptions.RequestException as e:
            self.stdout.write(self.style.ERROR(e))
