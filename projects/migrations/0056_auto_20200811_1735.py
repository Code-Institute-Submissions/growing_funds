# Generated by Django 3.0.8 on 2020-08-11 17:35

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0055_auto_20200811_1729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=ckeditor.fields.RichTextField(max_length=5000),
        ),
    ]
