from django.db import models
from django.contrib.auth.models import User

# Vendor Models

class Vendor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.TextField(null=True)
 
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