# Generated by Django 3.1.8 on 2021-07-11 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_auto_20210711_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberlist',
            name='position',
            field=models.CharField(max_length=30),
        ),
    ]
