from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Seller


def get_and_authenticate_user(email, password):
    user = authenticate(username=email, password=password)
    if user is None:
        raise serializers.ValidationError("Invalid username/password. Please try again!")
    return user


def create_account(email, password, is_seller=False,  **extra_fields):
    user = get_user_model().objects.create_user(
        email=email, password=password, is_seller=is_seller, **extra_fields)
    if is_seller:
        seller = Seller.objects.create(user = user)
    return user


def activate_seller(email):
    query = get_user_model().objects.filter(email = email).update(is_seller=True)
    print(query)
    # user.is_seller = True
    # user.update(is_seller=True)
    user = get_user_model().objects.get(email = email)
    print(user.email)
    print(user.is_seller)
    seller = Seller.objects.create(user = user)
    print(111)
    return user
