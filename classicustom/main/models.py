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
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title
