# Generated by Django 3.1.8 on 2021-07-01 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadphoto',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]