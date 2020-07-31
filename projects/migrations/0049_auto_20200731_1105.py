# Generated by Django 3.0.8 on 2020-07-31 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('projects', '0048_auto_20200731_1047'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='user',
        ),
        migrations.AddField(
            model_name='project',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=models.SET('deleted_user'), related_name='projects', to='profiles.UserProfile'),
        ),
    ]
