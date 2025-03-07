from rest_framework import serializers
from . import models


#  Vendors

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = ['user', 'address']
    
    def __init__(self, *args, **kwargs):
        super(VendorSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1 



class VendorDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Vendor
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(VendorDetailSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1 

# Products

class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ['id', 'title', 'description', 'price', 'sale_price', 'is_sale', 'category','vendor']

    def __init__(self, *args, **kwargs):
        super(ProductListSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1  

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductDetailSerializer, self).__init__(*args, **kwargs)
        # self.Meta.depth = 1  

#  CUstomer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ['id', 'user', 'mobile']

    def __init__(self, *args, **kwargs):
        super(CustomerSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1 

class CustomerDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CustomerDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1 


# Order

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Orders
        fields = ['id', 'customer']

    def __init__(self, *args, **kwargs):
        super(OrderSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1 

class OrderDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.OrderItems
        fields = ['id', 'order', 'product']

    def __init__(self, *args, **kwargs):
        super(OrderDetailSerializer, self).__init__(*args, **kwargs)
        self.Meta.depth = 1 