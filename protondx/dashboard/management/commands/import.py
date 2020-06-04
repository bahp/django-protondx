"""
This module is used to import patient data into the database using Django Import-Export.
"""

import os
import datetime
import random
from django.core.management.base import BaseCommand
from import_export import resources
from tablib import Dataset

from ...models import Patient, TestingCentre, DiagnosticTest

LOAD_PATIENT = 0
LOAD_CENTRE = 1
LOAD_DIAGNOSTIC = 2


def load_diagnostics(entries):
    """
    This method creates 'DiagnosticTest' database entries using pre-existing 'Patient' and 'TestingCentre' entries.
    Test results and dates are generated pseudo-randomly.

    :param int entries: Number of 'DiagnosticTest' entries to generate
    :return:
    """
    centre_ids = list(TestingCentre.objects.values_list('id', flat=True))
    patient_ids = list(Patient.objects.values_list('id', flat=True))

    start_dt = datetime.date.today().replace(day=1, month=1).toordinal()
    end_dt = datetime.date.today().toordinal()

    for i in range(entries):
        random_day = datetime.date.fromordinal(random.randint(start_dt, end_dt))
        random_time = str(random_day) + " " + str((random.randint(0, 23))) + ":" + str((random.randint(0, 59)))

        random_result = False if random.random() < 0.8 else True

        random_centre = random.choice(centre_ids)
        random_patient = random.choice(patient_ids)

        date = datetime.datetime.strptime(random_time, "%Y-%m-%d %H:%M")
        entry = DiagnosticTest(date_test=date,
                               test_result=random_result,
                               testing_centre=TestingCentre(random_centre),
                               patient=Patient(random_patient))
        entry.save()


# Create database entries
class Command(BaseCommand):
    """
    This command is used to load Patient data into the database

    -usage:
        manage.py import [-h] [-p] [-c] [-d] [--path PATH] [--version]
        [-v {0,1,2,3}] [--settings SETTINGS]
        [--pythonpath PYTHONPATH] [--traceback] [--no-color]
        [--force-color] [--skip-checks]

    -optional arguments:
        --h, --help:
            show this help message and exit
        --p, --patient:
            Upload patient data
        --c, --centre:
            Upload centre data
        --d, --diagnostic:
            Upload diagnostic data
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
        This method creates flags which identify which model is to be loaded and an
        optional '--path' argument which can be used to specify a file path when loading data.
        '--entries' is used to determine the number of 'DiagnosticTest entries to generate'
        """

        parser.add_argument("-p", "--patient",
                            action="store_const", const=LOAD_PATIENT, dest="obj_type", help='Upload patient data')
        parser.add_argument("-c", "--centre",
                            action="store_const", const=LOAD_CENTRE, dest="obj_type", help='Upload centre data')
        parser.add_argument("-d", "--diagnostic",
                            action="store_const", const=LOAD_DIAGNOSTIC, dest="obj_type", help='Upload diagnostic data')

        # Optional filepath argument
        parser.add_argument(
            '--path',
            type=str,
            help='File path to Patient dataset',
        )

        parser.add_argument(
            '--entries',
            type=int,
            help='Number of patient entries to generate ([-d] or [--diagnostic] must be set)',
        )

    def handle(self, *args, **options):
        """
        This method handles the command.

        It creates database entries for the specified model.
        If a file path is not provided default data will be loaded from 'protondx/dashboard/fixtures/'.
        """

        # Check if model to load was specified
        if options.get("obj_type", None) is not None:

            # If diagnostics are to be loaded, do so based on randomly generated data.
            if options['obj_type'] == LOAD_DIAGNOSTIC:
                load_diagnostics(options['entries'] or 1000)
                return

            model_info = {
                LOAD_PATIENT:
                    (resources.modelresource_factory(model=Patient)(), '../../fixtures/patient_mock.csv'),
                LOAD_CENTRE:
                    (resources.modelresource_factory(model=TestingCentre)(), '../../fixtures/centre_mock.csv'),
                LOAD_DIAGNOSTIC:
                    (resources.modelresource_factory(model=DiagnosticTest)(), '../../fixtures/diagnostic_mock.csv'),
            }

            # Check if a path was given, use default if not
            if options['path']:
                file_path = options['path']
            else:
                module_dir = os.path.dirname(__file__)  # get current directory
                file_path = os.path.join(module_dir, model_info[options['obj_type']][1])  # get data directory

            resource = model_info[options['obj_type']][0]

            # open data source
            with open(file_path, 'r') as f:
                dataset = Dataset().load(f.read(), format='csv')

            # import
            resource.import_data(dataset, dry_run=False, raise_errors=True)
        else:
            print("Please provide the model type of data: [--patient] [-p] [--centre] [-c] [--diagnostic] [-d]")
