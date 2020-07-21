from django.db import models
from django.contrib.auth.models import AbstractUser


from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import ugettext_lazy as _


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, first_name, last_name,  **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email,first_name=first_name, last_name=last_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField('First Name', max_length=255, blank=True,
                                  null=False)
    last_name = models.CharField('Last Name', max_length=255, blank=True,
                                 null=False)
    photo = models.ImageField(blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
    
    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"


class Adopter(CustomUser):

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Adopter'
        verbose_name_plural = 'Adopters'

## Seller and Adopter differentiates by permission class
## We need to set the view permission of backend services

class Seller(CustomUser):

    def __str__(self):
        return f"{self.email} - {self.first_name} {self.last_name}"

    class Meta:
        verbose_name = 'Seller'
        verbose_name_plural = 'Sellers'
