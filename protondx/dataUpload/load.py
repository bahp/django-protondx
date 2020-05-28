import os
from django.contrib.gis.utils import LayerMapping
from .models import CountryBorder

country_mapping = {
    'name': 'NAME',
    'mpoly': 'MULTIPOLYGON',
}

country_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'ne_50m_admin_0_countries.shp'),
)


def run(verbose=True):
    lm = LayerMapping(CountryBorder, country_shp, country_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
