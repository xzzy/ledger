# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2022-07-06 09:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0019_basket_booking_reference_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='no_oracle',
            field=models.NullBooleanField(default=False),
        ),
    ]
