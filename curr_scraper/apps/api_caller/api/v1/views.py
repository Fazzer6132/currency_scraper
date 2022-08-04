import django_filters
from api_caller.models import Currency, CurrencyRateRecord
from django.http import HttpResponse
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from curr_scraper.apps.api_caller.api.v1.serializers import CurrencySerializer, CurrencyRateRecordSerializer


def index(request):
    """Test response."""
    return HttpResponse("Hello!")


class CurrencyView(viewsets.ModelViewSet):
    """Get a list of all currencies."""
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer
    permission_classes = [IsAuthenticated]


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


class CurrencyRateView(viewsets.ModelViewSet):
    """Get a list of all currency rate records with optional filters."""
    queryset = CurrencyRateRecord.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatesFilter
    serializer_class = CurrencyRateRecordSerializer
    pagination_class = RatesPagination
    permission_classes = [IsAuthenticated]



