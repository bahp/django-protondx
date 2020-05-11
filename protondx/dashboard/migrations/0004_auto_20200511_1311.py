# Generated by Django 3.0.5 on 2020-05-11 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20200511_1135'),
    ]

    operations = [
        migrations.AddField(
            model_name='testingcentre',
            name='lat',
            field=models.FloatField(default=0, verbose_name='Latitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='testingcentre',
            name='lon',
            field=models.FloatField(default=0, verbose_name='Longitude'),
            preserve_default=False,
        ),
    ]