# Generated by Django 3.0.5 on 2020-05-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0010_auto_20200515_0959'),
    ]

    operations = [
        migrations.AddField(
            model_name='testingcentre',
            name='country',
            field=models.CharField(max_length=255, null=True, verbose_name='Country'),
        ),
        migrations.AddField(
            model_name='testingcentre',
            name='county',
            field=models.CharField(max_length=255, null=True, verbose_name='County'),
        ),
        migrations.AddField(
            model_name='testingcentre',
            name='region',
            field=models.CharField(max_length=255, null=True, verbose_name='Region'),
        ),
    ]
