# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-10-23 11:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0017_auto_20181023_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oracleinterfacededuction',
            name='oisystem',
        ),
        migrations.DeleteModel(
            name='OracleInterfaceDeduction',
        ),
    ]
