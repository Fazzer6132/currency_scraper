from django.db import models


class Currency(models.Model):
    """A model describing type of currency."""
    code = models.CharField()
    description = models.CharField()

    class Meta:
        app_label = "api_caller"
        verbose_name = "currency"
        verbose_name_plural = "currencies"


class CurrencyRateRecord(models.Model):
    """A model describing a singular record of conversion rate of a particular currency in terms of base currency."""
    timestamp = models.DateTimeField()
    curr = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='currency_rate_records')
    base_curr = models.ForeignKey(Currency, on_delete=models.PROTECT,
                                  related_name='base_currency_rate_records')
    rate = models.DecimalField()

    class Meta:
        app_label = "api_caller"
        verbose_name = "currency rate record"
        verbose_name_plural = "currency rate records"
