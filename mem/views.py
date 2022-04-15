from itertools import product
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.mixins import ListModelMixin,CreateModelMixin
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from .models import Product, Reviews
from .serializers import Productserializer, Reviewserializer
from rest_framework import status , generics

from mem import serializers

class ProductView(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = Productserializer

    def get_serializer_context(self):
        return {'request ': self.request}
    lookup_field = 'id'

class ReviewView(ModelViewSet):
    queryset = Reviews.objects.all()
    serializer_class = Reviewserializer



# class ProductList(ListCreateAPIView):
#     queryset = queryset = Product.objects.all()
#     serializer_class = Productserializer

#     def get_serializer_context(self):
#         return {'request ': self.request}




# class ProductDetails(RetrieveUpdateDestroyAPIView):
#     queryset = queryset = Product.objects.all()
#     serializer_class = Productserializer
#     lookup_field = 'id'

