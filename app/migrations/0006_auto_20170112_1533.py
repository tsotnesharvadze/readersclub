# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-12 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20170112_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorymodel',
            name='slug',
            field=models.SlugField(blank=True, max_length=250, null=True, unique=True),
        ),
    ]
