from decimal import Decimal
from rest_framework import serializers
from .models import product, Reviews, Userdata

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        field = {'id'}

class Productserializer(serializers.ModelSerializer) :
    class Meta:
        model = product
        fields = ('id','title','price','price_with_discount')
        Userdata = Userserializer()  
    price_with_discount = serializers.SerializerMethodField(method_name='calculate')

    def calculate(self , product : product):
        return product.price * Decimal(0.9)

class Favouriteserializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ('id','title','price','is_favourite')   


class Userserializer(serializers.ModelSerializer):
    class Meta:
        model = Userdata
        fields = ('id')


class Reviewserializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ['id', 'date', 'name', 'description']

    def create(self, validated_data):
        product_id = self.context['product_id']
        return Reviews.objects.create(product_id=product_id, **validated_data)             