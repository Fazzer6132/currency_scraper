from django.db import models


class Currency(models.Model):
    code = models.TextField()
    description = models.TextField()

    class Meta:
        app_label = "api_caller"


class CurrencyRateRecord(models.Model):
    timestamp = models.TimeField()
    curr = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='currency_name_records_currency')
    base_curr = models.ForeignKey(Currency, on_delete=models.PROTECT,
                                  related_name='currency_name_records_base_currency')
    rate = models.DecimalField()

    class Meta:
        app_label = "api_caller"
