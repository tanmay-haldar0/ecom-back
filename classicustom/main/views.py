from . import serializers
from rest_framework import generics, permissions
from . import models

class VendorList(generics.ListAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class = serializers.VendorSerializer
    # permission_classes = [permissions.IsAuthenticated]

class VendorDetail(generics.RetrieveAPIView):
    queryset=models.Vendor.objects.all()
    serializer_class = serializers.VendorDetailSerializer
    # permission_classes = [permissions.IsAuthenticated]