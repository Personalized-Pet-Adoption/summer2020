from rest_framework import serializers
from django.utils.timezone import datetime
from django.contrib.auth.models import User, Group
from .models import Pet



class UserSerializer(serializers.ModelSerializer):
    # pets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())
    class Meta:
        model = User
        fields = ['url', 'id', 'username' ,'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class PetSerializer(serializers.ModelSerializer):
    owner_id = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = Pet
        fields = ['id', 'name', 'owner_id','species', 'breed', 'postal_code','price','post_date','birthday','source_website','gender']