# Generated by Django 3.1.8 on 2021-07-11 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0008_auto_20210711_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='memberlist',
            name='position',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
