import django_filters
from api_caller.models import Currency, CurrencyRateRecord
from django.db import connection, OperationalError
from django.http import HttpResponse
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import CurrencySerializer, CurrencyRateRecordSerializer


def index(request):
    """Test response."""
    return HttpResponse("Hello!")


class CheckHealth(APIView):
    """Return "OK" if server is up."""
    def get(self, request):
        try:
            connection.ensure_connection()
        except OperationalError:
            content = {'Server status': 'Failed connection to database'}
            return Response(content, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        else:
            content = {'Server status': 'OK'}
            return Response(content, status=status.HTTP_200_OK)


class CurrencyView(generics.ListAPIView):
    """Get a list of all currencies."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class RatesPagination(PageNumberPagination):
    """Pagination class for CurrencyRateView."""
    page_size = 50


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """Abstract filter for Char+BaseIn inheritance."""
    pass


class RatesFilter(django_filters.FilterSet):
    """Filter for CurrencyRateRecords view."""
    curr = CharFilterInFilter(field_name='curr__code', lookup_expr='in')
    date = filters.DateFromToRangeFilter(field_name='dtime_created')

    class Meta:
        model = CurrencyRateRecord
        fields = ('curr',)


class CurrencyRateView(generics.ListAPIView):
    """Get a list of all currency rate records with optional filters."""
    queryset = CurrencyRateRecord.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatesFilter
    serializer_class = CurrencyRateRecordSerializer
    pagination_class = RatesPagination



