from decimal import Decimal
from pyexpat import model
from rest_framework import serializers
from .models import Product, Reviews, Userdata

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        field = {'id'}

class Productserializer(serializers.ModelSerializer) :
    class Meta:
        model = Product
        fields = ('id','title','price','price_with_discount')
        Userdata = Userserializer()  
    price_with_discount = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self , product : Product):
        return product.price * Decimal(0.9)


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = ('id')

class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('id','date','name','description','Product')       