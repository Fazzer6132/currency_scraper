from django.db import models


class RateRecord(models.Model):
    timestamp = models.DateTimeField('Date of record')
    UAHrate = models.FloatField('UAH to USD')
    GBPrate = models.FloatField('GBP to USD')
    EURrate = models.FloatField('EUR to USD')
    PLNrate = models.FloatField('PLN to USD')
