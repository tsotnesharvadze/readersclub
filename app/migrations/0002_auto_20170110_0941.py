# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 09:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookmodel',
            options={'verbose_name': 'წიგნი', 'verbose_name_plural': 'წიგნები'},
        ),
        migrations.AlterModelOptions(
            name='categorymodel',
            options={'verbose_name': 'კატეგორია', 'verbose_name_plural': 'კატეგორიები'},
        ),
    ]
