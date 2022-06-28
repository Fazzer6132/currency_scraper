from django.urls import path
from . import views


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path('', views.index, name='index'),
    path('sentry-debug/', trigger_error),
    path('health-check/', views.check_health),
    path('currencies/', views.get_currencies),
    path('currency-rates/', views.get_rates)
]