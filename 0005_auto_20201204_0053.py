# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2020-12-04 05:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0004_auto_20201204_0004'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sharedusers',
            name='note',
        ),
        migrations.RemoveField(
            model_name='note',
            name='id',
        ),
        migrations.AlterField(
            model_name='note',
            name='user',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.DeleteModel(
            name='SharedUsers',
        ),
    ]
