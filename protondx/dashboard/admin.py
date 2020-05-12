from django.contrib import admin
from django.contrib.gis import forms

# Register your models here.
from .models import Patient, DiagnosticTest


class TestInLine(admin.TabularInline):
    model = DiagnosticTest
    extra = 3


class PatientAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Patient Information', {'fields': ['first_name', 'last_name', 'dob', 'gender']}),
    ]

    inlines = [TestInLine]

    list_display = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name']


class LocationAdminForm(forms.ModelForm):
    coordinates = forms.PointField(widget=forms.OSMWidget(attrs={
        'display_raw': False}))


class DiagnosticTestAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date_test', 'test_result', 'postcode']
    fieldsets = [
        ('Test Information', {'fields': ['patient', 'date_test', 'test_result', 'coordinates', 'postcode', 'centre_type']}),
    ]
    form = LocationAdminForm


admin.site.register(Patient, PatientAdmin)
admin.site.register(DiagnosticTest, DiagnosticTestAdmin)
