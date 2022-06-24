from django.db import models
from django.utils.translation import ugettext_lazy as _


class Currency(models.Model):
    """A model describing type of currency."""
    code = models.CharField(max_length=4)
    description = models.CharField(max_length=25)

    class Meta:
        app_label = "api_caller"
        verbose_name = "currency"
        verbose_name_plural = "currencies"


class CurrencyRateRecord(models.Model):
    """A model describing a singular record of conversion rate of a particular currency in terms of base currency."""
    timedate = models.DateTimeField(auto_now_add=True)
    curr = models.ForeignKey(Currency, on_delete=models.PROTECT, related_name='currency_rate_records',
                             verbose_name=_(u'Currency'))
    base_curr = models.ForeignKey(Currency, on_delete=models.PROTECT,
                                  related_name='base_currency_rate_records', verbose_name=_(u'Currency (Base)'))
    rate = models.DecimalField(max_digits=20, decimal_places=4)

    class Meta:
        app_label = "api_caller"
        verbose_name = "currency rate record"
        verbose_name_plural = "currency rate records"
