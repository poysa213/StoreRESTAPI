from cgitb import lookup
from django.urls import path
from rest_framework import routers
from rest_framework_nested import routers
from . import views



router = routers.DefaultRouter()
router.register('product', views.ProductView)

product_routers = routers.NestedDefaultRouter(router,'product',lookup='Product')
product_routers.register('reviews',views.ReviewView)



# URLConf
urlpatterns = router.urls + product_routers.urls
