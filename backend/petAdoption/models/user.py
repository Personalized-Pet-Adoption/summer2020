from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
# from .pet import Pet


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
    # favorites = models.ManyToManyField(Pet, related_name='adopter', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Adopter'
        verbose_name_plural = 'Adopters'


class Seller(CustomUser):
    # pets_on_sale = models.ManyToManyField(Pet, related_name='seller', blank=True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
