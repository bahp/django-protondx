# Generated by Django 3.0.5 on 2020-05-28 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_diagnostictest_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testingcentre',
            name='country',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='testingcentre',
            name='county',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='County'),
        ),
        migrations.AlterField(
            model_name='testingcentre',
            name='postcode',
            field=models.CharField(blank=True, max_length=8, null=True, verbose_name='Postcode'),
        ),
        migrations.AlterField(
            model_name='testingcentre',
            name='region',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Region'),
        ),
    ]