# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 21:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='active',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
