"""
This module contains the Admin page definitions for the Dashboard App.
"""

from django.contrib import admin
from django.contrib.gis import forms

# Import import/export libraries
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
from .models import Patient, TestingCentre, DiagnosticTest


# Inline display of tests for patient and testing centre admin views
class TestInLine(admin.TabularInline):
    model = DiagnosticTest
    extra = 3


# Patient admin view
class PatientAdmin(ImportExportActionModelAdmin,
                   ImportExportModelAdmin):
    """
    This class defines the look of the PatientAdmin page.

        .. note: Diagnostic tests are displayed as in-line elements

    """
    fieldsets = [
        ('Patient Information', {'fields': ['first_name', 'last_name', 'dob', 'gender', 'postcode']}),
    ]

    inlines = [TestInLine]

    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


# Diagnostic test admin view
class DiagnosticTestAdmin(ImportExportActionModelAdmin,
                          ImportExportModelAdmin):
    """
    This class defines the look of the DiagnosticTestAdmin page.

        .. note: It allows to search by patient name, test date and test result.

    """
    fieldsets = [
        ('Test Information', {'fields': ['patient', 'testing_centre', 'date_test', 'test_result']}),
        ('Raw test data', {'fields': ['raw_test_data']})
    ]

    list_display = ['patient', 'date_test', 'test_result']
    search_fields = ['patient', 'date_test', 'test_result']


class TestingCentreAdminForm(forms.ModelForm):
    """
    Form used to input coordinates into a PointField using a map or textbox.
    """
    coordinates = forms.PointField(widget=forms.OSMWidget(attrs={
        'display_raw': True}))


# Testing Centre admin view
class CentreAdmin(ImportExportActionModelAdmin,
                  ImportExportModelAdmin):
    """
    This class defines the look of the CentreAdmin page.

        .. note: Diagnostic tests are displayed as in-line elements.

        .. note: It allows to search by centre type and postcode.

        ..note: A form is used for coordinates selection. It displays a map and textbox.

    """
    inlines = [TestInLine]
    list_display = ['centre_type', 'postcode', 'latitude', 'longitude']
    search_fields = ['centre_type', 'postcode']
    form = TestingCentreAdminForm


# Register all admin views
admin.site.register(Patient, PatientAdmin)
admin.site.register(DiagnosticTest, DiagnosticTestAdmin)
admin.site.register(TestingCentre, CentreAdmin)
