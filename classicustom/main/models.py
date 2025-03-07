from django.db import models
from django.contrib.auth.models import User

# Vendor Models

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)

    def __str__(self):
        return self.user.username
 
# Product Category

class ProductCategory(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField(null=True)

    def __str__(self):
        return self.title

# Product

class Product(models.Model):
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE)
    title = models.TextField(max_length=100, default="Title")
    description = models.TextField(max_length=500, default="Descriptions...")
    price = models.FloatField(default=000.00)
    review = models.FloatField(default=5.0)
    sale_price = models.FloatField(default=000.00)
    is_sale = models.BooleanField(default=False,)
    is_customizable = models.BooleanField(default=False,)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name='category_product')

    def __str__(self):
        return self.title

# Customer Model

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    mobile = models.PositiveBigIntegerField()

    def __str__(self):
        return self.user.username

#  Order Model

class Orders(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order_time = models.DateTimeField(auto_now_add=True)

class OrderItems(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, related_name='order_item')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.product.title