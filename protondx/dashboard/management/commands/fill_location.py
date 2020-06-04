"""
This module is used to fill coordinate and location data in a 'TestingCentre' dataset.
"""

import os
import pandas as pd

from django.core.management.base import BaseCommand
from ...fixtures.gen_location import generate_random


# Create database entries
class Command(BaseCommand):
    """
    This command is used to fill coordinate and location data in a Centre dataset.

    -usage:
        manage.py fill_location [-h] [--path PATH] [--version] [-v {0,1,2,3}]
        [--settings SETTINGS] [--pythonpath PYTHONPATH]
        [--traceback] [--no-color] [--force-color]
        [--skip-checks]

    -optional arguments:
        --h, --help:
            show this help message and exit
        ---path PATH:
            File path to Patient dataset
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
        ---traceback :
            Raise on CommandError exceptions
        ---no-color :
            Don't colorize the command output.
        ---force-color :
            colorization of the command output.
        ---skip-checks :
            Skip system checks.
    """

    def add_arguments(self, parser):
        """
        This method creates and optional '--path' argument which can be used to specify a file path when loading data.
        """

        # Optional filepath argument
        parser.add_argument(
            '--path',
            type=str,
            help='File path to Patient dataset',
        )

    def handle(self, *args, **options):
        """
        This method handles the command.

        It fills location columns of a 'TestingCentre' dataset.
        If a file path is not provided default data will be loaded from 'protondx/dashboard/fixtures/'.
        """

        # Check if a path was given, use default if not
        if options['path']:
            file_path = options['path']
        else:
            module_dir = os.path.dirname(__file__)  # get current directory
            file_path = os.path.join(module_dir, '../../fixtures/centre_mock.csv')  # get data directory

        df = pd.read_csv(file_path, dtype={'id': "Int64",
                                           'centre_type': str,
                                           'coordinates': str,
                                           'country': str,
                                           'region': str,
                                           'county': str,
                                           'postcode': str})

        count = df['coordinates'].isnull().sum()

        locations = generate_random(count)
        location_index = 0

        for index, row in df.iterrows():
            if pd.isnull(row['coordinates']):
                df.at[index, 'coordinates'] = str(locations[location_index]['coordinates'])
                df.at[index, 'country'] = locations[location_index]['country']
                df.at[index, 'region'] = locations[location_index]['region']
                df.at[index, 'county'] = locations[location_index]['county']
                df.at[index, 'postcode'] = locations[location_index]['postcode']
                location_index += 1

        df.to_csv(file_path, index=False)
