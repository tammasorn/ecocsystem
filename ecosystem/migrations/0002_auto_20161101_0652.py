# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-11-01 06:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecosystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='register',
            name='title',
            field=models.CharField(choices=[('นาย/Mr.', 'นาย/Mr'), ('นาง/Mrs.', 'นาง/Mrs'), ('นางสาว/Ms.', 'นางสาว/Ms')], max_length=1),
        ),
    ]
