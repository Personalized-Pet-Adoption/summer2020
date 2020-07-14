from rest_framework import serializers
from django.utils.timezone import datetime
# from django.contrib.auth.models import User, Group
from .models import Pet, CustomUser, Seller



# class UserSerializer(serializers.ModelSerializer):
#     # pets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())
#     class Meta:
#         model = CustomUser
#         fields = ['url', 'id', 'username']

class PetSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())
    class Meta:
        model = Pet
        fields = ['url','id', 'name', 'seller','species','price','post_date','gender']

class SellerSerializer(serializers.HyperlinkedModelSerializer):
    pets = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())
    class Meta:
        model = Seller
        fields = ['url', 'id', 'email', 'pets']


