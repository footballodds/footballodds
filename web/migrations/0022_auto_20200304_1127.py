# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2020-03-04 03:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_auto_20200304_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bigsmall',
            name='handicap',
            field=models.FloatField(blank=True, db_column='Handicap', default='0'),
        ),
        migrations.AlterField(
            model_name='letball',
            name='Handicap',
            field=models.FloatField(default='0'),
        ),
        migrations.AlterField(
            model_name='letball',
            name='left',
            field=models.FloatField(db_column='left', default=0),
        ),
        migrations.AlterField(
            model_name='letball',
            name='right',
            field=models.FloatField(default=0),
        ),
    ]
