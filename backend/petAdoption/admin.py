from django.contrib import admin
from .models import Pet
from .models import Immune
from .models import Image
from .models import Adopter
from .models import Seller

"""
Superuser already created:
    Username: pet_adoption_admin
    password: summer_2020_pet_admin_root
"""

# Register your models here.
admin.site.register(Adopter)
admin.site.register(Seller)
admin.site.register(Pet)
admin.site.register(Immune)
admin.site.register(Image)