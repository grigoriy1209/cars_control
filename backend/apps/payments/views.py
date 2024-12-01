from django.views.generic import TemplateView

from apps.payments.services import PaymentService


class ExchangeRatesView(TemplateView):
    template_name = 'rate_currency.html'

    def get_context_data(self, **kwargs):
        exchange_rates = PaymentService.get_currency_exchange_rates()

        context = super().get_context_data(**kwargs)
        context.update({
            'usd_uah': exchange_rates['USD_UAH'],
            'eur_uah': exchange_rates['EUR_UAH'],
            'usd_eur': exchange_rates['USD_EUR'],
        })
        return context
