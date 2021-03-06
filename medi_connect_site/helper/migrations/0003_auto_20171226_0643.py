# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-12-26 12:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helper', '0002_auto_20171224_0513'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='is_feedback',
        ),
        migrations.RemoveField(
            model_name='document',
            name='is_origin',
        ),
        migrations.RemoveField(
            model_name='order',
            name='auto_assigned',
        ),
        migrations.RemoveField(
            model_name='order',
            name='feedback',
        ),
        migrations.RemoveField(
            model_name='order',
            name='latest_upload',
        ),
        migrations.RemoveField(
            model_name='order',
            name='origin',
        ),
        migrations.RemoveField(
            model_name='order',
            name='pending',
        ),
        migrations.AddField(
            model_name='document',
            name='type',
            field=models.IntegerField(default=-1),
        ),
        migrations.AlterField(
            model_name='order',
            name='c2e_re_assigned',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.Customer'),
        ),
        migrations.AlterField(
            model_name='order',
            name='e2c_re_assigned',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='order',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helper.Patient'),
        ),
        migrations.AlterField(
            model_name='order',
            name='patient_order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='helper.OrderPatient'),
        ),
    ]
