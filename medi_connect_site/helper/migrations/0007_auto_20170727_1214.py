# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 04:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0006_auto_20170727_1211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='submit',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 27, 4, 14, 9, 598721, tzinfo=utc)),
        ),
    ]
