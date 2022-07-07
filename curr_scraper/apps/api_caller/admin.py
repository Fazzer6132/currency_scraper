from django.contrib import admin
from api_caller.models import Currency, CurrencyRateRecord


class CurrencyAdmin(admin.ModelAdmin):
    readonly_fields = ['code']
    search_fields = ['code']
    ordering = ['code']

class CurrencyRateRecordAdmin(admin.ModelAdmin):
    exclude = ['dtime_created', 'dtime_updated']
    readonly_fields = ['curr', 'base_curr']
    search_fields = ['curr__code', 'base_curr__code']
    ordering = ['dtime_updated']


admin.site.register(Currency, CurrencyAdmin)
admin.site.register(CurrencyRateRecord, CurrencyRateRecordAdmin)
