from django.shortcuts import render
from rest_framework import viewsets
from api9.models import Products
from api9.serializers import ProductSerializer

# Create your views here.

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer