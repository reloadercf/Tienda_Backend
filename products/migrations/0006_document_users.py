# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-08 23:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0005_document_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='users',
            field=models.ManyToManyField(related_name='documents', to=settings.AUTH_USER_MODEL),
        ),
    ]
