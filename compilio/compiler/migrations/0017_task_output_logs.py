# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-06-01 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compiler', '0016_auto_20170601_1250'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='output_logs',
            field=models.TextField(blank=True, null=True),
        ),
    ]
