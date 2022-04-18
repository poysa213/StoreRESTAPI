from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.viewsets import ModelViewSet
from mem.filters import ProductFilter
from .models import Product, Reviews
from .serializers import Productserializer, Reviewserializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title']
    ordering_fields = ['price']
    def get_serializer_context(self):
        return {'request ': self.request}
    lookup_field = 'id'
    

class ReviewView(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = Reviewserializer


