# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-07 02:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0004_auto_20171002_1518'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='document_complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.IntegerField(default=0),
        ),
    ]
