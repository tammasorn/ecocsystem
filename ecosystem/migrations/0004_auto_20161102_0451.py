# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-02 04:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecosystem', '0003_auto_20161101_0841'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='address_1',
            field=models.CharField(default=0, max_length=500, verbose_name='Address'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='city',
            field=models.CharField(default=0, max_length=100, verbose_name='City'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='register',
            name='province',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
