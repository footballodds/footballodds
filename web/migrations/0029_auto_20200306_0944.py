# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-06 01:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_auto_20200306_0901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigsmall',
            name='updatetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 9, 44, 2, 556929)),
        ),
        migrations.AlterField(
            model_name='companyodds',
            name='updatetime',
            field=models.DateTimeField(db_column='Updatetime', default=datetime.datetime(2020, 3, 6, 9, 44, 2, 557927)),
        ),
        migrations.AlterField(
            model_name='letball',
            name='updatetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 9, 44, 2, 560919)),
        ),
        migrations.AlterField(
            model_name='winalone',
            name='updatetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 6, 9, 44, 2, 562913)),
        ),
    ]
