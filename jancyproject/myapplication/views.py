from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Account, Destination
from .serializers import AccountSerializer, DestinationSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def perform_destroy(self, instance):
        instance.destinations.all().delete()
        instance.delete()

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer

    def perform_destroy(self, instance):
        instance.delete()

    @action(detail=True, methods=['get'])
    def get_destinations_for_account(self, request, pk=None):
        account = Account.objects.get(pk=pk)
        destinations = Destination.objects.filter(account=account)
        serializer = self.get_serializer(destinations, many=True)
        return Response(serializer.data)

# Create your views here.
