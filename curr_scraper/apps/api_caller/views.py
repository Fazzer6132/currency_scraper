from django.http import HttpResponse
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import CurrencySerializer, CurrencyRateRecordSerializer
from api_caller.models import Currency, CurrencyRateRecord


def index(request):
    return HttpResponse("Hi dude")


@api_view(['GET'])
def check_health(request):
    content = {'Server status': 'OK'}
    return Response(content, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_currencies(request):
    items = Currency.objects.all()
    serializer = CurrencySerializer(items, many=True)
    return Response(serializer.data)


class rates_pagination(PageNumberPagination):
    page_size = 50


@api_view(['GET'])
def get_rates(request):
    items = CurrencyRateRecord.objects.all()
    serializer = CurrencyRateRecordSerializer(items, many=True)
    pagination_class = rates_pagination
    return Response(serializer.data)
