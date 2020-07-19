from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


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

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Adopter'
        verbose_name_plural = 'Adopters'


class Seller(CustomUser):

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
