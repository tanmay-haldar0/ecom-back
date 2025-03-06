from rest_framework import serializers
from . import models

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = '__all__'

class VendorDetailSerializer(serializers.HyperlinkedRelatedField):
    class Meta:
        model = models.Vendor
        fields = '__all__'