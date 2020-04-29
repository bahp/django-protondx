# Generic
import datetime

# Basic libraries
from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Import import/export libraries
#from import_export import resources

# Import simple history library
#from simple_history.models import HistoricalRecords



class Device(models.Model):
  """This contains the Device attributes.

    .. note: Using p_attrname to indicate properties
    .. note: Using m_attrname to indicate methods
    .. note: In templates attribute cannot start with _.

  """
  # -----------------------
  # Definitions
  # -----------------------

  # Dates
  # -----
  date_created = models.DateTimeField(auto_now_add=True,
    verbose_name='Date created')
  date_updated = models.DateTimeField(auto_now=True,
    verbose_name='Date updated')
  date_acquired = models.DateTimeField(
    verbose_name='Date acquired')

  # Parameters
  # -----------
  euid = models.CharField(max_length=200, unique=True,
    verbose_name='External UID')
  manufacturer = models.CharField(max_length=200,
    verbose_name='Manufacturer')





class Cartridge(models.Model):
  """This contains the Cartridge attributes.

    .. note: Using p_attrname to indicate properties
    .. note: Using m_attrname to indicate methods
    .. note: In templates attribute cannot start with _.

  """
  # -----------------------
  # Definitions
  # -----------------------
  
  # Dates
  # -----
  date_created = models.DateTimeField(auto_now_add=True,
    verbose_name='Date created')
  date_updated = models.DateTimeField(auto_now=True,
    verbose_name='Date updated')
  date_acquired = models.DateTimeField(
    verbose_name='Date acquired')

  # Parameters
  # -----------
  euid = models.CharField(max_length=200, unique=True,
    verbose_name='External UID')
  manufacturer = models.CharField(max_length=200,
    verbose_name='Manufacturer')




class Experiment(models.Model):
  """This contains the experiment attributes.

    .. note: Should it be called differently? diagnostic? outcome?
    .. note: Should we use on_delete=models.PROTECT instead?
    .. note:
  """
  # -----------------------
  # Definitions
  # -----------------------
  DISEASE_CHOICES = [
      ('MALARIA', 'Malaria'),
      ('DENGUE', 'Dengue'),
      ('CHIKUNGUNYA', 'Chikungunya'),
      ('COVID19', 'COVID19')
  ]

  # Dates
  # -----
  date_created = models.DateTimeField(auto_now_add=True,
    verbose_name='Date created')
  date_updated = models.DateTimeField(auto_now=True,
    verbose_name='Date updated')
  date_experiment = models.DateTimeField(
    verbose_name='Date experiment')

  # Foreign Keys
  # ------------
  device = models.ForeignKey(Device,
    on_delete=models.CASCADE)
  cartridge = models.ForeignKey(Cartridge,
    on_delete=models.CASCADE)

  # Parameters
  # ----------
  disease = models.CharField(max_length=200,
    verbose_name='Disease',
    choices=DISEASE_CHOICES)
  concentration = models.FloatField(blank=True,
    verbose_name='Concentration (mmol/L)',
    validators=[MinValueValidator(0), MaxValueValidator(1000)],
    help_text='The concentration of the microorganism in the sample.')
