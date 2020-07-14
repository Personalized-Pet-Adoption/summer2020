from django.db import models
from django.utils.timezone import datetime
from ..models.user import Seller

class Pet(models.Model):
    name = models.CharField(max_length=64)
    owner = models.ForeignKey(Seller, on_delete=models.CASCADE)
    species = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    breed = models.CharField(max_length=64, blank=True)
    postal_code = models.IntegerField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    post_date = models.DateField(default=datetime.now)
    birthday = models.DateField(null=True, blank=True)
    # age can be infer
    #age = models.IntegerField(blank=True)
    source_website = models.CharField(max_length=200,blank=True)
    gender = models.CharField(max_length=64)
    weight = models.FloatField(null=True)

    def __str__(self):
        return self.name


class Image(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    # TODO:
    # Not sure if this is correct
    # maybe need to set max possible file size? 
    # should we validate photo front end/backend (same thing for email address)
    # front end provide link or image?
    # image = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')


class Immune(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    neuter = models.BooleanField(default=False)
    heartgard = models.BooleanField(default=False)
    nexgard = models.BooleanField(default=False)
    rabies = models.DateField(null=True)
    da2pp = models.DateField(null=True)
    intra2 = models.DateField(null=True)
    extrainfo = models.TextField(null=True)
    record_date = models.DateField()