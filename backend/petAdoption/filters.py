from django_filters import rest_framework as filters
from .models.pet import Pet
from accounts.models import Seller

class PetFilter(filters.FilterSet):
    min_price = filters.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = filters.NumberFilter(field_name="price", lookup_expr='lte')
    min_age = filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_age = filters.NumberFilter(field_name='age', lookup_expr='lte')
    min_weight = filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_weight = filters.NumberFilter(field_name='age', lookup_expr='lte')
    species_contain = filters.CharFilter(field_name='species', lookup_expr='icontains')
    breed_contain = filters.CharFilter(field_name='breed', lookup_expr='icontains')
    species = filters.CharFilter(field_name='species', lookup_expr='iexact')
    breed = filters.CharFilter(field_name='breed', lookup_expr='iexact')
    gender = filters.CharFilter(field_name='gender', lookup_expr='iexact')
    class Meta:
        model: Pet
        fields: ['species','species_contain','breed','breed_contain','gender','min_price', 'max_price', 'min_age','max_age', 'min_weight','max_weight']


class SellerFilter(filters.FilterSet):
    name = filters.CharFilter(field_name="name", lookup_expr='icontains')
    class Meta:
        model: Seller
        fields: ['name']