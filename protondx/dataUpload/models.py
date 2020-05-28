from django.contrib.gis.db import models


class CountryBorder(models.Model):
    name = models.CharField(max_length=255)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name


class RegionBorder(models.Model):
    name = models.CharField(max_length=255)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name


class PostcodeBorder(models.Model):
    name = models.CharField(max_length=255)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name
