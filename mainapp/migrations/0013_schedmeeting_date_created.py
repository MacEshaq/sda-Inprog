# Generated by Django 3.1.8 on 2021-07-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0012_schedmeeting'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedmeeting',
            name='date_created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
