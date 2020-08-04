from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Seller, Adopter

def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user

def create_adopter_account(email, password,first_name="",
                        last_name="", is_adopter=False, is_seller=False,  **extra_fields):
    user = get_user_model().objects.create_user(
        email=email, password=password, first_name=first_name,
        last_name=last_name, is_adopter=True, is_seller=is_seller, **extra_fields)
    seller = Adopter.objects.create(user = user)
    return user


def create_seller_account(email, password,first_name="",
                        last_name="", is_adopter=False, is_seller=False, **extra_fields):
    user = get_user_model().objects.create_user(
        email=email, password=password, first_name=first_name,
        last_name=last_name, is_adopter=is_adopter, is_seller=True, **extra_fields)
    seller = Seller.objects.create(user = user)
    return user