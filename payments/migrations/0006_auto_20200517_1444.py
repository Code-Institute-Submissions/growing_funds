# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-17 12:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0005_auto_20200517_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='project',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, to='projects.Project'),
        ),
    ]