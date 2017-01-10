# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-27 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_auto_20161227_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='address',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='მისამართი'),
        ),
        migrations.AlterField(
            model_name='account',
            name='born',
            field=models.DateField(blank=True, null=True, verbose_name='დაბადების თარიღი'),
        ),
        migrations.AlterField(
            model_name='account',
            name='experience',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='გამოცდილება'),
        ),
        migrations.AlterField(
            model_name='account',
            name='home_phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='სახ.ტელეფონი'),
        ),
        migrations.AlterField(
            model_name='account',
            name='location',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='მდებარეობა'),
        ),
        migrations.AlterField(
            model_name='account',
            name='phone',
            field=models.IntegerField(blank=True, null=True, verbose_name='მობ.ტელეფონი'),
        ),
        migrations.AlterField(
            model_name='account',
            name='profession',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='პროფესია'),
        ),
        migrations.AlterField(
            model_name='account',
            name='status',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='სტატუსი'),
        ),
        migrations.AlterField(
            model_name='account',
            name='work_time',
            field=models.DateField(blank=True, max_length=40, null=True, verbose_name='მუშაობის დაწყების დრო'),
        ),
    ]