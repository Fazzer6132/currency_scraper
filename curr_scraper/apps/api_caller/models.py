from django.db import models


class Currency(models.Model):
    code = models.TextField()
    description = models.TextField()

    class Meta:
        app_label = "api_caller"


class CurrencyRateRecord(models.Model):
    timestamp = models.TimeField()
    curr = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='%(class)s_currency')
    base_curr = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='%(class)s_base_currency')
    rate = models.FloatField()

    class Meta:
        app_label = "api_caller"
