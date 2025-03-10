# Generated by Django 5.1.6 on 2025-03-06 09:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='contact_person',
        ),
        migrations.RemoveField(
            model_name='vendor',
            name='name',
        ),
        migrations.AddField(
            model_name='vendor',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
    ]
