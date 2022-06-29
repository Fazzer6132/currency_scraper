import django_filters
from api_caller.models import Currency, CurrencyRateRecord
from django.http import HttpResponse
from django_filters import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from .serializers import CurrencySerializer, CurrencyRateRecordSerializer


def index(request):
    """Test response"""
    return HttpResponse("Hello!")


@api_view(['GET'])
def check_health(request):
    """Return "OK" if server is up"""
    content = {'Server status': 'OK'}
    return Response(content, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_currencies(request):
    """Get a list of all currency types"""
    items = Currency.objects.all()
    serializer = CurrencySerializer(items, many=True)
    return Response(serializer.data)


class RatesPagination(PageNumberPagination):
    """Pagination class for CurrencyRateView"""
    page_size = 50


class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    """Abstract filter for Char+BaseIn inheritance"""
    pass


class RatesFilter(django_filters.FilterSet):
    """Filter for CurrencyRateRecords view"""
    curr = CharFilterInFilter(field_name='curr__code', lookup_expr='in')
    date = filters.DateFromToRangeFilter(field_name='dtime_created')


    class Meta:
        model = CurrencyRateRecord
        fields = ('curr',)


class CurrencyRateView(generics.ListAPIView):
    """Get a list of all currency rate records"""
    queryset = CurrencyRateRecord.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = RatesFilter
    filterset_fields = {
        'start_date':['gte', 'lte', 'exact', 'gt', 'lt'],
        'end_date':['exact'],
                        }
    serializer_class = CurrencyRateRecordSerializer
    pagination_class = RatesPagination



