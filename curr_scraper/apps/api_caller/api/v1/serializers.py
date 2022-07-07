from api_caller.models import Currency, CurrencyRateRecord
from rest_framework import serializers


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class CurrencyRateRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRateRecord
        fields = '__all__'
