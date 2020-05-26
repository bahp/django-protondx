from django.contrib import admin
from django.contrib.gis import forms

# Register your models here.
from .models import Patient, TestingCentre, DiagnosticTest


# Inline display of tests for patient and testing centre admin views
class TestInLine(admin.TabularInline):
    model = DiagnosticTest
    extra = 3


# Patient admin view
class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Patient Information', {'fields': ['first_name', 'last_name', 'dob', 'gender', 'postcode']}),
    ]

    inlines = [TestInLine]

    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


# Diagnostic test admin view
class DiagnosticTestAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Test Information', {'fields': ['patient', 'testing_centre', 'date_test', 'test_result']}),
        ('Raw test data', {'fields': ['raw_test_data']})
    ]

    list_display = ['patient', 'date_test', 'test_result']
    search_fields = ['patient', 'date_test', 'test_result']


# Form to input coordinates using a Map or a textbox
class TestingCentreAdminForm(forms.ModelForm):
    coordinates = forms.PointField(widget=forms.OSMWidget(attrs={
        'display_raw': True}))


# Testing Centre admin view
class CentreAdmin(admin.ModelAdmin):
    inlines = [TestInLine]
    list_display = ['centre_type', 'postcode', 'latitude', 'longitude']
    search_fields = ['centre_type', 'postcode']
    form = TestingCentreAdminForm


# Register all admin views
admin.site.register(Patient, PatientAdmin)
admin.site.register(DiagnosticTest, DiagnosticTestAdmin)
admin.site.register(TestingCentre, CentreAdmin)
