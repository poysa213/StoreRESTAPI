from argparse import Action
from inspect import Parameter
from itertools import product
from turtle import title
from django.urls import reverse
from django.contrib import admin
from django.db.models.query import QuerySet
from . import models
from django.contrib.admin import SimpleListFilter

class roomsfilter(admin.SimpleListFilter):
    title = 'Rooms'
    parameter_name = 'Rooms'

    def lookups(self, request, model_admin):
        return [
            ('1', 'F1'),
            ('2', 'F2'),
            ('3', 'F3'),
            ('4', 'F4'),
            ('5', 'F5'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '1':
            return queryset.filter(Rooms=1)
        if self.value() == '2':
            return queryset.filter(Rooms=2)
        if self.value() == '3':
            return queryset.filter(Rooms=3)
        if self.value() == '4':
            return queryset.filter(Rooms=4)
        if self.value() == '5':
            return queryset.filter(Rooms=5)



@admin.register(models.Product)
class ProdcutAdmin(admin.ModelAdmin) :
    actions = ['clear_price']
    list_display = ['title','price']
    list_per_page = 10
    list_filter = [roomsfilter]
    search_fields = ['title__istartswith','Rooms__istartswith']



    @admin.action(description="clear price")
    def clear_price(self, request, queryset):
        updated_count = queryset.update(price=0)
        self.message_user(
            request,
            f'{updated_count} products were successfully updated.'
        )
