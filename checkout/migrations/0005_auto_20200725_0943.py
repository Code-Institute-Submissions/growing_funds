# Generated by Django 3.0.8 on 2020-07-25 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0004_merge_20200725_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='reward',
            field=models.CharField(choices=[('Option 1', 'Option 1'), ('Option 2', 'Option 2'), ('Option 3', 'Option 3'), ('Nothing', 'Nothing')], default='Nothing', max_length=9),
        ),
    ]
