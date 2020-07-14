from rest_framework import serializers
from django.utils.timezone import datetime
from django.contrib.auth.models import User, Group
from .models import Pet



class UserSerializer(serializers.ModelSerializer):
    pets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())
    class Meta:
        model = User
        fields = ['url', 'id', 'username' ,'groups', 'pets']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    class Meta:
        model = Pet
        fields = ['id', 'name', 'owner','species','price','post_date','gender']