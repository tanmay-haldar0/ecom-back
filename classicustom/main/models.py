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
    titel = models.TextField()
    price = models.FloatField()
    sale_price = models.FloatField()
    is_sale = models.BooleanField(default=False)
    product_category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)