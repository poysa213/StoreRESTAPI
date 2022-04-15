from ctypes.wintypes import SIZE
from multiprocessing import pool
from turtle import title
from unicodedata import name
from django.db import models


class Userdata(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    Birthdate = models.DateTimeField(auto_now=False, auto_now_add=False)

class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(null=True)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=8, decimal_places=0,null=True)
    Rooms = models.DecimalField(max_digits=2,decimal_places=0,null=True)
    Size = models.DecimalField(max_digits=8,decimal_places=4,null=True)
    Wifi = models.BooleanField(null=True)
    Equipped = models.BooleanField(null=True)
    Parking = models.BooleanField(null=True)
    Created = models.DateTimeField(auto_now=True)
    pool = models.BooleanField(null=True)
    phone = models.DecimalField(max_digits=10, decimal_places=0,null=True)
    def __str__(self) -> str:
        return self.title
    class Meta:
        ordering = ['title']

class Reviews(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE , related_name='reviews')
    name = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)