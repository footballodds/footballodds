# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2020-03-02 07:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_auto_20200302_1453'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bigsmall',
            name='gameinfo',
        ),
        migrations.RemoveField(
            model_name='letball',
            name='gameinfo',
        ),
        migrations.RemoveField(
            model_name='winalone',
            name='gameinfo',
        ),
    ]
