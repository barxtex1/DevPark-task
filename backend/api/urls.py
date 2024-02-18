from django.urls import path

from .views import (
    CurrencyExchangeView,
    CurrenciesListView
)


urlpatterns = [
    path('exchange/', CurrencyExchangeView.as_view(), name='currency-exchange'),
    path('currencies/', CurrenciesListView.as_view(), name='currency-list'),
]
