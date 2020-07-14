from .models import Pet
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pet
from .serializers import PetSerializer, UserSerializer, GroupSerializer
from rest_framework import viewsets
from rest_framework import generics

from rest_framework import permissions
from rest_framework.decorators import action
# Create your APIs here.



class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer



class PetViewSet(viewsets.ModelViewSet):
    """
    List all pets (first 50, ordered by post date), 
    or add a new pet.
    """
    queryset = Pet.objects.order_by('-post_date')[:50]
    serializer_class = PetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# Format

# {
#     "name": "abc",
#     "species": "gg",
#     "post_date": "2020-07-10",
#     "gender": "Female"
# }