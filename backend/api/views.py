from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Currencies

from .serializers import (
    CurrencyExchangeSerializer,
    CurrenciesSerializer
)
from cfehome.settings import API_KEY



class CurrenciesListView(ListAPIView):
    queryset = Currencies.objects.all()
    serializer_class = CurrenciesSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['code']



class CurrencyExchangeView(APIView):

    def get(self, request, *args, **kwargs):
        serializer = CurrencyExchangeSerializer(data=request.query_params, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            
            return Response({"status": True})