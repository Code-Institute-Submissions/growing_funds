# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-16 13:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fundlineitem',
            name='amount',
        ),
        migrations.AddField(
            model_name='fund',
            name='amount',
            field=models.IntegerField(default=0),
        ),
    ]
