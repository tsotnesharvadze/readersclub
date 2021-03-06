# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-10 09:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0009_auto_20161229_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='address',
        ),
        migrations.RemoveField(
            model_name='account',
            name='avatar',
        ),
        migrations.RemoveField(
            model_name='account',
            name='born',
        ),
        migrations.RemoveField(
            model_name='account',
            name='experience',
        ),
        migrations.RemoveField(
            model_name='account',
            name='home_phone',
        ),
        migrations.RemoveField(
            model_name='account',
            name='location',
        ),
        migrations.RemoveField(
            model_name='account',
            name='profession',
        ),
        migrations.RemoveField(
            model_name='account',
            name='status',
        ),
        migrations.RemoveField(
            model_name='account',
            name='tagline',
        ),
        migrations.RemoveField(
            model_name='account',
            name='username',
        ),
        migrations.RemoveField(
            model_name='account',
            name='work_time',
        ),
        migrations.AddField(
            model_name='account',
            name='personal_number',
            field=models.IntegerField(default=1, verbose_name='პირადი ნომერი'),
        ),
        migrations.AddField(
            model_name='account',
            name='rules',
            field=models.BooleanField(default=False, verbose_name='წესები'),
        ),
    ]
