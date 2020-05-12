# Generated by Django 3.0.5 on 2020-05-12 07:13

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_auto_20200511_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diagnostictest',
            name='testing_centre',
        ),
        migrations.AddField(
            model_name='diagnostictest',
            name='centre_type',
            field=models.CharField(choices=[('HOSP', 'Hospital'), ('CLIN', 'GP clinic'), ('DRIV', 'Drive through centre'), ('HOME', 'Home'), ('OTHR', 'Other')], default='OTHR', max_length=4, verbose_name='Centre type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='diagnostictest',
            name='coordinates',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326, verbose_name='Coordinates'),
        ),
        migrations.AddField(
            model_name='diagnostictest',
            name='postcode',
            field=models.CharField(max_length=8, null=True, verbose_name='Postcode'),
        ),
        migrations.DeleteModel(
            name='TestingCentre',
        ),
    ]
