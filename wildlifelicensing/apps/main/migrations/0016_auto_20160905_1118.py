# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-05 03:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wl_main', '0015_auto_20160901_1436'),
    ]

    operations = [
        migrations.RenameField(
            model_name='communicationslogentry',
            old_name='officer',
            new_name='staff',
        ),
    ]
