# Generated by Django 5.1.6 on 2025-03-07 06:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productcategory_alter_vendor_address_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='review',
            field=models.FloatField(default=5.0),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.productcategory'),
        ),
    ]
