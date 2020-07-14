from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .pet import Pet
from .managers import CustomUserManager
# TODO:
# class User(models.Model):
#     ## TODO: Shall we implement this????
#     ## django already has a User class built in that controls
#     ## whether the user has authority to change or update specific database table
#     pass


class CustomUser(AbstractUser):
    username = models.CharField(max_length=255)
    email = models.EmailField(_('email address'), unique=True)
    password = models.CharField(max_length=255)
    photo = models.ImageField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.username


class Adopter(CustomUser):
    favorites = models.ManyToManyField(Pet, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Adopter'
        verbose_name_plural = 'Adopters'


class Seller(CustomUser):
    pets_on_sale = models.ManyToManyField(Pet, blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
