from django.db import models
from django.contrib.auth.models import User


class Pet(models.Model):
    name = models.CharField(max_length=64)
    desciption = models.TextField()
    breed = models.CharField(max_length=64)
    postal_code = models.IntegerField()
    # use float or double?
    price = models.FloatField()
    date = models.DateField()
    birthday = models.DateField()
    age = models.IntegerField()
    species = models.CharField(max_length=200)
    source_website = models.CharField(max_length=200)
    gender = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    # Many-to-one foreign key to User id
    # it should be user id
    # TODO: uncomment this line after User class has been set
    # owner = models.ForeignKey(User, on_delete=models.CASCADE)


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
    # TODO: for Yiping Zhong
    # research on what do we need to store for immune record for a pet
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    record_date = models.DateField()


# TODO:
# Question: Shall we create this?
# Maybe try inheriting the django built in user class?
# class User(models.Model):
#     ## TODO: Shall we implement this????
#     ## django already has a User class built in that controls
#     ## whether the user has authority to change or update specific database table
#     pass


class Adopter(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Pet)

    def __str__(self):
        return self.user.username


class Seller(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pets_on_sale = models.ManyToManyField(Pet)

    def __str__(self):
        return self.user.username
