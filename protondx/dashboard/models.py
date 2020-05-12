from django.db import models
from django.contrib.gis.db import models as geomodels

# Create your models here.
from django.contrib.gis.geos import Point


class Patient(models.Model):
    """
    This class contains basic patient information.
    """

    # -----------------------
    # Definitions
    # -----------------------
    FEMALE = 'F'
    MALE = 'M'
    OTHER = 'O'
    PREFER_NOT_SAY = ''

    GENDER = [
        (FEMALE, 'Female'),
        (MALE, 'Male'),
        (OTHER, 'Other'),
        (PREFER_NOT_SAY, 'Prefer not to say'),
    ]

    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    gender = models.CharField(max_length=1, null=True, choices=GENDER, verbose_name='Gender')
    dob = models.DateField(null=True, verbose_name='Date of birth')
    postcode = models.CharField(max_length=8, null=True, verbose_name='Postcode')  # This assumes standard UK

    # postcode. If other countries are to be added the max_length must be revised

    def __str__(self):
        return self.last_name + ", " + self.first_name


class DiagnosticTest(models.Model):
    """
    This class contains information for diagnostic tests
    """

    # -----------------------
    # Definitions
    # -----------------------

    # Dates
    # -----
    date_test = models.DateTimeField(verbose_name='Test date')

    # Foreign Keys
    # ------------
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # Parameters
    #  ----------

    POS = True
    NEG = False

    DIAGNOSIS = [
        (POS, 'Positive'),
        (NEG, 'Negative'),
    ]
    test_result = models.BooleanField(choices=DIAGNOSIS, verbose_name='Test result')

    HOSPITAL = 'HOSP'
    CLINIC = 'CLIN'
    DRIVE_THROUGH = 'DRIV'
    HOME_TEST_SITE = 'HOME'
    OTHER_TEST_SITE = 'OTHR'

    CENTRE_TYPE = [
        (HOSPITAL, 'Hospital'),
        (CLINIC, 'GP clinic'),
        (DRIVE_THROUGH, 'Drive through centre'),
        (HOME_TEST_SITE, 'Home'),
        (OTHER_TEST_SITE, 'Other'),
    ]

    centre_type = models.CharField(max_length=4, choices=CENTRE_TYPE, verbose_name='Centre type')
    coordinates = geomodels.PointField(verbose_name='Coordinates', null=True)
    postcode = models.CharField(max_length=8, null=True, verbose_name='Postcode')  # This assumes standard UK
    # postcode. If other countries are to be added the max_length must be revised

    def __str__(self):
        return self.patient.last_name + ", " + self.patient.first_name + ": " + str(self.date_test)
