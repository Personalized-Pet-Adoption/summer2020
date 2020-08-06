from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.authentication import TokenAuthentication
from django_filters import rest_framework as filters
from .filters import PetFilter
from rest_framework.filters import OrderingFilter

class PetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    filter_backends = (filters.DjangoFilterBackend, OrderingFilter)
    filterset_class = PetFilter



