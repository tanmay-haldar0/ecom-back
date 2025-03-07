from . import serializers
from rest_framework import generics, permissions
from . import models

class VendorList(generics.ListCreateAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer

class VendorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer 

class ProductList(generics.ListAPIView):
    queryset=models.Product.objects.all()
    serializer_class = serializers.ProductListSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=models.Product.objects.all()
    serializer_class = serializers.ProductDetailSerializer
