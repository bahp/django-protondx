# General
from django.contrib import admin

# Register your models here.

# Import models
from . import models
#from . import filters

# Import import/export libraries
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


# --------------------------------------------------------------------
#            enable export/import from django package
# --------------------------------------------------------------------
# This export/import functionality is provided by the external
# package django-import-export. Refer to the documentation for
# more information on how to use and configure the package.
#
# In order to add the functionality to the admin page the classes
# created in this file (e.g. SubmissionAdmin) need to extend the
# ImportExportActionModelAdmin (if action in table view page), 
# ImportExportModelAdmin (for whole exporting) or both.
#
# .. note: Move to another file?
# 
# Possible meta attributes:
#  fields :
#  include : 
#  exclude :
#  export_order :
#  import_id_fields :
#  skip_unchanged :
#  report_skipped :
#  widgets : {}

class DeviceResource(resources.ModelResource):
  class Meta:
      model = models.Device

class CartridgeResource(resources.ModelResource):
  class Meta:
      model = models.Cartridge

class ExperimentResource(resources.ModelResource):
  class Meta:
      model = models.Experiment


# --------------------------------------------------------------------
#                            DEVICE
# --------------------------------------------------------------------
@admin.register(models.Device)
class DeviceAdmin(ImportExportActionModelAdmin,
                  ImportExportModelAdmin):
    """This class defines the look of the device admin page.

    .. note: It allows to filter by ...
    .. note: It allows to search by ...

    .. note: It extends the classes (ImportExportActionModelAdmin,
             and ImportExportModelAdmin) from the django external
             package django-import-export. This allows to import/
             export the data. 

    .. note: The default class to extend in the admin package 
             would have been admin.modelAdmin.

    """
    # -------------------------
    # Override text field form
    # -------------------------
    # Override
    #formfield_overrides = {}

    # -------------------------
    # Save configuration
    # -------------------------
    # Save
    save_as = True       # Add button save as new
    save_on_top = False  # Put buttons on top

    # -------------------------
    # Ordering
    # -------------------------
    ordering = ('-date_created',)

    # -------------------------
    # Filter by time
    # -------------------------
    # Filter by time
    #date_hierarchy = 'timestamp'

    # -------------------------
    # Fields to search
    # -------------------------
    # Fields to search
    search_fields = ['euid']

    # -------------------------
    # Fields to filter
    # -------------------------
    # Fields to filter for
    list_filter = ['manufacturer']

    # -------------------------
    # Read only fields
    # -------------------------
    # Read only fields
    readonly_fields = ['date_created', 'date_updated']

    # -------------------------
    # Fields to display in list
    # -------------------------
    # Fields to display in list
    list_display = ['id',
                    'euid',
                    'date_created',
                    'date_updated',
                    'date_acquired',
                    'manufacturer']

    # ----------------------------
    # Groups to present the fields
    # ----------------------------
    # How to group the elements
    fieldsets = [
        ('ID',
            {'fields': ['euid']}),
        ('Metadata',
            {'fields': ['date_created',
                        'date_updated',
                        'date_acquired']}),
        ('Information',
            {'fields': ['manufacturer']})
    ]






# --------------------------------------------------------------------
#                            CARTRIDGE
# --------------------------------------------------------------------
@admin.register(models.Cartridge)
class CartridgeAdmin(ImportExportActionModelAdmin,
                     ImportExportModelAdmin):
    """This class defines the look of the cartridgeadmin page.

    .. note: It allows to filter by ...
    .. note: It allows to search by ...

    .. note: It extends the classes (ImportExportActionModelAdmin,
             and ImportExportModelAdmin) from the django external
             package django-import-export. This allows to import/
             export the data. 

    .. note: The default class to extend in the admin package 
             would have been admin.modelAdmin.

    """
    # -------------------------
    # Override text field form
    # -------------------------
    # Override
    #formfield_overrides = {}

    # -------------------------
    # Save configuration
    # -------------------------
    # Save
    save_as = True       # Add button save as new
    save_on_top = False  # Put buttons on top

    # -------------------------
    # Ordering
    # -------------------------
    ordering = ('-date_created',)

    # -------------------------
    # Filter by time
    # -------------------------
    # Filter by time
    #date_hierarchy = 'timestamp'

    # -------------------------
    # Fields to search
    # -------------------------
    # Fields to search
    search_fields = ['euid']

    # -------------------------
    # Fields to filter
    # -------------------------
    # Fields to filter for
    list_filter = ['manufacturer']

    # -------------------------
    # Read only fields
    # -------------------------
    # Read only fields
    readonly_fields = ['date_created', 'date_updated']

    # -------------------------
    # Fields to display in list
    # -------------------------
    # Fields to display in list
    list_display = ['id',
                    'euid',
                    'date_created',
                    'date_updated',
                    'date_acquired',
                    'manufacturer']

    # ----------------------------
    # Groups to present the fields
    # ----------------------------
    # How to group the elements
    fieldsets = [
        ('ID',
            {'fields': ['euid']}),
        ('Metadata',
            {'fields': ['date_created',
                        'date_updated',
                        'date_acquired']}),
        ('Information',
            {'fields': ['manufacturer']})
    ]



# --------------------------------------------------------------------
#                            EXPERIMENT
# --------------------------------------------------------------------
@admin.register(models.Experiment)
class ExperimentAdmin(ImportExportActionModelAdmin,
                      ImportExportModelAdmin):
    """This class defines the look of the experiment admin page.

    .. note: It allows to filter by ...
    .. note: It allows to search by ...

    .. note: It extends the classes (ImportExportActionModelAdmin,
             and ImportExportModelAdmin) from the django external
             package django-import-export. This allows to import/
             export the data. 

    .. note: The default class to extend in the admin package 
             would have been admin.modelAdmin.

    """
    # -------------------------
    # Override text field form
    # -------------------------
    # Override
    #formfield_overrides = {}

    # -------------------------
    # Save configuration
    # -------------------------
    # Save
    save_as = True       # Add button save as new
    save_on_top = False  # Put buttons on top

    # -------------------------
    # Ordering
    # -------------------------
    ordering = ('-date_created',)

    # -------------------------
    # Filter by time
    # -------------------------
    # Filter by time
    #date_hierarchy = 'timestamp'

    # -------------------------
    # Fields to search
    # -------------------------
    # Fields to search
    search_fields = ['euid']

    # -------------------------
    # Fields to filter
    # -------------------------
    # Fields to filter for
    list_filter = ['device',
                   'disease']

    # -------------------------
    # Read only fields
    # -------------------------
    # Read only fields
    readonly_fields = ['date_created', 'date_updated']

    # -------------------------
    # Fields to display in list
    # -------------------------
    # Fields to display in list
    list_display = ['id',
                    'date_created',
                    'date_updated',
                    'date_experiment',
                    'device',
                    'cartridge',
                    'disease',
                    'concentration']

    # ----------------------------
    # Groups to present the fields
    # ----------------------------
    # How to group the elements
    fieldsets = [
        ('Metadata',
            {'fields': ['date_created',
                        'date_updated',
                        'date_experiment']}),
        ('Instruments',
            {'fields': ['device',
                        'cartridge']}),
        ('Outcome',
            {'fields': ['disease',
                        'concentration']}),
    ]