from django.db import models
from django.contrib.gis.db import models as geomodels
from .choices import GENDER, CENTRE_TYPE, DIAGNOSIS


# Patient model (can contain any information related to the patient)
# Patient has 0 or more tests
class Patient(models.Model):
    """
    This class contains basic patient information.
    """

    # -----------------------
    # Definitions
    # -----------------------

    first_name = models.CharField(max_length=50, verbose_name='First name')
    last_name = models.CharField(max_length=50, verbose_name='Last name')
    gender = models.CharField(max_length=1, null=True, choices=GENDER, verbose_name='Gender')
    dob = models.DateField(null=True, blank=True, verbose_name='Date of birth')
    postcode = models.CharField(max_length=8, null=True, blank=True, verbose_name='Postcode')  # This assumes standard UK

    # postcode. If other countries are to be added the max_length must be revised

    def __str__(self):
        return self.last_name + ", " + self.first_name


# Testing Centre model (can contain any information related to the centre/area where a Diagnostic test may be held)
# has 0 or more tests associated to it
class TestingCentre(geomodels.Model):
    """
    This class contains testing centre information
    """

    # -----------------------
    # Definitions
    # -----------------------

    centre_type = models.CharField(max_length=20, choices=CENTRE_TYPE, verbose_name='Centre type')
    coordinates = geomodels.PointField(verbose_name='Coordinates')
    country = models.CharField(max_length=255, null=True, blank=True, verbose_name='Country')
    region = models.CharField(max_length=255, null=True, blank=True, verbose_name='Region')
    county = models.CharField(max_length=255, null=True, blank=True, verbose_name='County')
    postcode = models.CharField(max_length=8, null=True, blank=True, verbose_name='Postcode')  # This assumes
    # standard UK postcode. If other countries are to be added the max_length must be revised

    @property
    def latitude(self):
        if self.coordinates:
            return self.coordinates.y

    @property
    def longitude(self):
        if self.coordinates:
            return self.coordinates.x


# Diagnostic Test model (contains all information related to the test, i.e. date, result, patient, testing_centre...)
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
    testing_centre = models.ForeignKey(TestingCentre, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)

    # Parameters
    #  ----------

    test_result = models.BooleanField(choices=DIAGNOSIS, verbose_name='Test result')
    comment = models.TextField(null=True, blank=True)
    raw_test_data = models.FileField(upload_to='uploads/', null=True, blank=True, verbose_name='Raw Test Data')

    def __str__(self):
        return self.patient.last_name + ", " + self.patient.first_name + ": " + str(self.date_test)
