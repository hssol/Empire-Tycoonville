# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-03-29 23:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Empire_App', '0008_market_snapshot_snapshot_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='market_snapshot',
            name='snapshot_datetime',
            field=models.CharField(max_length=255),
        ),
    ]
