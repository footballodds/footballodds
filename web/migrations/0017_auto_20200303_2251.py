# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-03-03 14:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0016_auto_20200303_1305'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companyodds',
            name='updatetime',
            field=models.TimeField(blank=True, db_column='Updatetime', null=True),
        ),
    ]
