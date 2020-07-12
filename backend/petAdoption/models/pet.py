from django.db import models


class Pet(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()
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
    weight = models.FloatField(null=True)

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