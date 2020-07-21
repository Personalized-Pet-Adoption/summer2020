from rest_framework import serializers
from .models import *
from accounts.models import *


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


class AdopterSerializer(serializers.HyperlinkedModelSerializer):
    favorites = serializers.PrimaryKeyRelatedField(many=True, queryset=Pet.objects.all())

    class Meta:
        model = Adopter
        fields = ['url', 'id', 'email', 'favorites']
