# Generated by Django 3.0.5 on 2020-05-26 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0011_auto_20200525_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='diagnostictest',
            name='raw_test_data',
            field=models.FileField(null=True, upload_to='uploads/', verbose_name='Raw Test Data'),
        ),
    ]