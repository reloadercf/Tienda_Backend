# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 23:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_auto_20170425_2144'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='product',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='products.Product'),
            preserve_default=False,
        ),
    ]
