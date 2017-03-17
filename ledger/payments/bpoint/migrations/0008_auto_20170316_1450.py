# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bpoint', '0007_usedbpointtoken'),
    ]

    operations = [
        migrations.AddField(
            model_name='bpointtransaction',
            name='dvtoken',
            field=models.CharField(blank=True, help_text='Stored card dv token', max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='bpointtransaction',
            name='last_digits',
            field=models.CharField(blank=True, help_text='Last four digits of card used during checkout', max_length=4, null=True),
        ),
    ]
