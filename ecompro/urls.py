from django.urls import path
from .views import *

urlpatterns = [
    path('base/',base, name='base'),
    path('',index, name='home'),
    path('about/',about, name='about'),
    path('blog/',blog, name='blog'),
    path('contact/',contact, name='contact'),
    path('products/',product, name='product'),
]
