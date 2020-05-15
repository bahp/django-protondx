# Generated by Django 3.0.5 on 2020-05-14 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20200513_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testingcentre',
            name='centre_type',
            field=models.CharField(choices=[('Hospital', 'Hospital'), ('GP clinic', 'GP clinic'), ('Drive through centre', 'Drive through centre'), ('Home', 'Home'), ('Other', 'Other')], max_length=20, verbose_name='Centre type'),
        ),
    ]
