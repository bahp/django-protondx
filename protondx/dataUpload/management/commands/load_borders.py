"""
This module is used to populate the various Border tables in the database.
It extracts location data from shape and project files under 'dataUpload/data'.
"""

import os
from django.contrib.gis.utils import LayerMapping
from ...models import CountryBorder, RegionBorder, CountyBorder, PostcodeBorder
from django.core.management.base import BaseCommand

country_mapping = {
    'name': 'NAME',
    'mpoly': 'MULTIPOLYGON',
}

country_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../data', 'ne_50m_admin_0_countries.shp'),
)

region_mapping = {
    'name': 'nuts118nm',
    'mpoly': 'MULTIPOLYGON',
}

region_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../data', 'NUTS_Level_1__January_2018__Boundaries_WGS_84.shp'),
)

county_mapping = {
    'name': 'ctyua19nm',
    'mpoly': 'MULTIPOLYGON',
}

county_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../../data',
                 'Counties_and_Unitary_Authorities__December_2019__Boundaries_UK_BGC_WGS_84.shp'),
)


# Create database entries
class Command(BaseCommand):
    """
    This command is used to load border data into the database.

    -usage:
        manage.py load_borders [-h] [--country] [--region] [--county]
        [--verbose] [--version] [-v {0,1,2,3}]
        [--settings SETTINGS] [--pythonpath PYTHONPATH]
        [--traceback] [--no-color] [--force-color]
        [--skip-checks]

    -optional arguments:
        --h, --help:
            show this help message and exit
        ---country:
            Store country borders
        ---region:
            Store country borders
        ---county:
            Store county borders
        ---verbose:
            Verbose
        ---version:
            show program's version number and exit
        --v {0,1,2,3}, --verbosity {0,1,2,3}:
            Verbosity level; 0=minimal output, 1=normal output,
            2=verbose output, 3=very verbose output
        ---settings SETTINGS:
            The Python path to a settings module, e.g.
            "myproject.settings.main". If this isn't provided, the
            DJANGO_SETTINGS_MODULE environment variable will be
            used.
        ---pythonpath PYTHONPATH:
            A directory to add to the Python path, e.g.
            "/home/djangoprojects/myproject".
        ---traceback:
            Raise on CommandError exceptions
        ---no-color:
            Don't colorize the command output.
        ---force-color:
            Force colorization of the command output.
        ---skip-checks:
            Skip system checks.
    """

    def add_arguments(self, parser):
        """
        This method creates flags which identify what borders are to be loaded into the database.
        """

        parser.add_argument(
            '--country',
            action='store_true',
            dest='country',
            help='Store country borders',
        )

        parser.add_argument(
            '--region',
            action='store_true',
            dest='region',
            help='Store country borders',
        )

        parser.add_argument(
            '--county',
            action='store_true',
            dest='county',
            help='Store county borders',
        )

        parser.add_argument(
            '--verbose',
            action='store_true',
            dest='verbose',
            help='Verbose',
        )

    def handle(self, *args, **options):
        """
        This method handles the command and adds Region and Country Borders to the database.
        """

        if not options['country'] and not options['region'] and not options['county']:
            print("Please select borders to be loaded to database. For help try: manage.py load_borders -h")

        if options['country']:
            lm_country = LayerMapping(CountryBorder, country_shp, country_mapping, transform=False)
            lm_country.save(strict=True, verbose=options['verbose'])
            print("Country borders loaded.")
        if options['region']:
            lm_region = LayerMapping(RegionBorder, region_shp, region_mapping, transform=False)
            lm_region.save(strict=True, verbose=options['verbose'])
            print("Region borders loaded.")
        if options['county']:
            lm_county = LayerMapping(CountyBorder, county_shp, county_mapping, transform=False)
            lm_county.save(strict=True, verbose=options['verbose'])
            print("County borders loaded.")

