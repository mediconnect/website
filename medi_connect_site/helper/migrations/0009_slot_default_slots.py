# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-07 20:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0008_remove_slot_default_slots'),
    ]

    operations = [
        migrations.AddField(
            model_name='slot',
            name='default_slots',
            field=models.IntegerField(default=20),
        ),
    ]
