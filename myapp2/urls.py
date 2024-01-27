from django.urls import path
from .views import create_product


app_name = 'myapp2'

urlpatterns = [
    
    path('create_product/', create_product, name='create_product'),

]