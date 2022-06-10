from django.db import models


class Currency(models.Model):
    code = models.TextField()
    description = models.TextField()


class RateRecord(models.Model):
    timestamp = models.TimeField()
    currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    base_currency = models.ForeignKey(Currency, on_delete=models.PROTECT)
    rate = models.FloatField()
