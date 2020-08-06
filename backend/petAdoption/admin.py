from django.contrib import admin

from .models import *
from accounts.models import *
from django.contrib.auth import get_user_model

"""
Superuser already created:
    Username: pet_adoption_admin
    password: summer_2020_pet_admin_root
"""

myModels = [Pet, Immune, Image]
admin.site.register(myModels)

User = get_user_model()

@admin.register(User)
class AdopterInline(admin.ModelAdmin):
    model = User


@admin.register(Seller)
class SellerInline(admin.ModelAdmin):
    model = Seller




