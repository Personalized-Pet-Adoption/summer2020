from django.shortcuts import render
from .models import Pet
from django.http import HttpResponse

from django.core import serializers

# Create your views here.

# return the data of first 50 pets ordered by post date
def get_all_pets(request):
    pet_list = Pet.objects.order_by('-post_date')[:50]
    output = serializers.serialize("json", pet_list)
    return HttpResponse(output)