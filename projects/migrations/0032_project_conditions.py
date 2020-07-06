# Generated by Django 3.0.7 on 2020-07-06 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0031_remove_project_conditions'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='conditions',
            field=models.BooleanField(default=False, error_messages={'required': 'Please agree to our terms and conditions'}, null=True),
        ),
    ]
