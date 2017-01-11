# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-11 12:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20170110_0941'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='sex',
            field=models.CharField(choices=[('0', '-----'), ('1', 'მამრობითი'), ('2', 'მდედრობითი')], default='0', max_length=1, verbose_name='სქესი'),
        ),
    ]
