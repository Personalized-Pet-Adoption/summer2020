from .models import Pet
from django.contrib.auth.models import User, Group
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Pet
from .serializers import PetSerializer, UserSerializer, GroupSerializer
from rest_framework import viewsets

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



class PetView(APIView):
    """
    List all pets (first 50, ordered by post date), 
    or add a new pet.
    """
    def get(self, request):
        pets = Pet.objects.order_by('-post_date')[:50]
        serializer = PetSerializer(pets, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = PetSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

