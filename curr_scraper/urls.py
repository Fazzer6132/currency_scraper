"""curr_scraper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from curr_scraper.apps.api_caller.api.v1.views import CurrencyView, CurrencyRateView
from curr_scraper import views


def trigger_error(request):
    division_by_zero = 1 / 0


router = routers.DefaultRouter()
router.register('currencies', CurrencyView)
router.register('currency_rates', CurrencyRateView)
urlpatterns = [
    path('health-check', views.CheckHealth.as_view()),
    path('admin/', admin.site.urls),
    path('sentry-debug', trigger_error),
    path('api/v1/', include(router.urls)),
    path('o/', include('oauth2_provider.urls', namespace='oauth2_provider'))
]

