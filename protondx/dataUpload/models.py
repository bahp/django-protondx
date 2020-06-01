from django.contrib.gis.db import models


class CountryBorder(models.Model):
    """This contains the CountryBorder attributes."""

    name = models.CharField(max_length=255)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name


class RegionBorder(models.Model):
    """This contains the RegionBorder attributes."""

    name = models.CharField(max_length=255)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name


class PostcodeBorder(models.Model):
    """This contains the PostcodeBorder attributes."""

    name = models.CharField(max_length=255)
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name
