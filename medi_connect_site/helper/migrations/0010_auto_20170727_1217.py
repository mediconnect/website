# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 04:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0009_auto_20170727_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='submit',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
