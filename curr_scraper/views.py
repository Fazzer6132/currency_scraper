from django.db import connection, OperationalError
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


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