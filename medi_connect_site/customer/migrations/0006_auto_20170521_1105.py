# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-21 15:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_auto_20170326_0304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='date',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='telephone',
        ),
        migrations.AddField(
            model_name='customer',
            name='email',
            field=models.EmailField(default=b'unkown', max_length=254),
        ),
        migrations.AddField(
            model_name='customer',
            name='qq',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='register_time',
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name='customer',
            name='tel',
            field=models.TextField(default=b'unkown'),
        ),
        migrations.AddField(
            model_name='customer',
            name='wechat',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='customer',
            name='weibo',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='zipcode',
            field=models.IntegerField(default=0),
        ),
    ]
