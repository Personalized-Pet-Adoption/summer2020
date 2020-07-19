from .serializers import *
from rest_framework import viewsets
from rest_framework import permissions


class SellerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Seller.objects.all().order_by('-date_joined')
    serializer_class = SellerSerializer


class AdopterViewSet(viewsets.ModelViewSet):
    queryset = Adopter.objects.all().order_by('-date_joined')
    serializer_class = AdopterSerializer


class PetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


