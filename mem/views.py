from rest_framework.viewsets import ModelViewSet
from mem.filters import ProductFilter
from .models import product, Reviews
from .serializers import Productserializer, Reviewserializer,Favouriteserializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
from django.shortcuts import get_object_or_404





class ProductView(ModelViewSet):
    queryset = product.objects.all()
    serializer_class = Productserializer
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    filterset_class = ProductFilter
    search_fields = ['title']
    ordering_fields = ['price']
    def get_serializer_context(self):
        return {'request ': self.request}
    lookup_field = 'id'
    

class ReviewView(ModelViewSet):
    serializer_class = Reviewserializer

    def get_queryset(self):
        return Reviews.objects.filter(product_id=self.kwargs['product_pk'])

    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}
















class FavouriteView(ModelViewSet):
    serializer_class =  Favouriteserializer
    def get_queryset(self):
        return product.objects.filter(is_favourite = True)
    def get_serializer_context(self):
        return {'product_id': self.kwargs['product_pk']}    


