# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-02 04:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecosystem', '0004_auto_20161102_0451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='address_1',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='register',
            name='city',
            field=models.CharField(max_length=100),
        ),
    ]