# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-18 18:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_mainproduct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainproduct',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='product', to='products.Product'),
        ),
    ]
