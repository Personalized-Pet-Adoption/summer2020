from django.contrib import admin

from .models import *
from accounts.models import *

"""
Superuser already created:
    Username: pet_adoption_admin
    password: summer_2020_pet_admin_root
"""

myModels = [Pet, Immune, Image]
admin.site.register(myModels)


@admin.register(Adopter)
class AdopterInline(admin.ModelAdmin):
    model = Adopter


@admin.register(Seller)
class SellerInline(admin.ModelAdmin):
    model = Seller




