# Generated by Django 5.1.6 on 2025-03-07 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_is_customizable'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='titel',
            new_name='title',
        ),
    ]
