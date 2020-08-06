from rest_framework import serializers
from .models import *
from accounts.models import Seller
from django.contrib.auth import get_user_model

User = get_user_model()

class PetSerializer(serializers.ModelSerializer):
    seller = serializers.PrimaryKeyRelatedField(queryset=Seller.objects.all())

    class Meta:
        model = Pet
        fields = ['url','id', 'name', 'seller','species','price','post_date','gender']



