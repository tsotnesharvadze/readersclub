# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-01-15 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0015_readersclubmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='readersclubmodel',
            name='contact_address',
            field=models.CharField(default='', max_length=200, null=True, verbose_name='მისამართი (კონტაქტი)'),
        ),
        migrations.AddField(
            model_name='readersclubmodel',
            name='contact_email',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='ემაილი (კონტაქტი)'),
        ),
        migrations.AddField(
            model_name='readersclubmodel',
            name='contact_phone',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='ტელეფონი (კონტაქტი)'),
        ),
    ]
