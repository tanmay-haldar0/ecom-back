# Generated by Django 5.1.6 on 2025-03-07 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_product_description_alter_product_titel'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_customizable',
            field=models.BooleanField(default=False),
        ),
    ]
