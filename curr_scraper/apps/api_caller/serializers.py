from rest_framework import serializers
from api_caller.models import Currency, CurrencyRateRecord


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = '__all__'


class CurrencyRateRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CurrencyRateRecord
        fields = '__all__'
