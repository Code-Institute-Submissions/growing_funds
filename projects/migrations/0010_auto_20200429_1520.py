# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-04-29 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_auto_20200428_1719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='goal',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='project',
            name='raised',
            field=models.IntegerField(default=0),
        ),
    ]