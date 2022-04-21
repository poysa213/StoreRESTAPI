from dataclasses import fields
from django_filters.rest_framework import FilterSet
from mem.models import product

class ProductFilter(FilterSet):
    class Meta:
        model = product
        fields = {
            'price': ['lt','gt']
        }