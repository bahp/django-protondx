# Generated by Django 3.0.5 on 2020-05-11 04:44

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20200511_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testingcentre',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(srid=4326, verbose_name='Coordinates'),
        ),
    ]
