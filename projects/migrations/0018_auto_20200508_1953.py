# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-08 17:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_auto_20200508_1927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]
