from dataclasses import fields
from django_filters.rest_framework import FilterSet
from mem.models import Product

class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = {
            'price': ['lt','gt']
        }