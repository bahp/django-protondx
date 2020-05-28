import os
from django.contrib.gis.utils import LayerMapping
from .models import CountryBorder, RegionBorder

country_mapping = {
    'name': 'NAME',
    'mpoly': 'MULTIPOLYGON',
}

country_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'ne_50m_admin_0_countries.shp'),
)


region_mapping = {
    'name': 'nuts118nm',
    'mpoly': 'MULTIPOLYGON',
}

region_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'NUTS_Level_1__January_2018__Boundaries.shp'),
)


def run(verbose=True):
    lm_country = LayerMapping(CountryBorder, country_shp, country_mapping, transform=False)
    lm_country.save(strict=True, verbose=verbose)
    lm_region = LayerMapping(RegionBorder, region_shp, region_mapping, transform=False)
    lm_region.save(strict=True, verbose=verbose)
