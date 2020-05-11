from django.contrib import admin
from django.contrib.gis import forms

# Register your models here.
from .models import Patient, TestingCentre, DiagnosticTest


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


class DiagnosticTestAdmin(admin.ModelAdmin):
    list_display = ['patient', 'date_test', 'test_result']
    fieldsets = [
        ('Test Information', {'fields': ['patient', 'testing_centre', 'date_test', 'test_result']}),
    ]





class TestingCentreAdminForm(forms.ModelForm):
    coordinates = forms.PointField(widget=forms.OSMWidget(attrs={
        'display_raw': False}))


class CentreAdmin(admin.ModelAdmin):
    inlines = [TestInLine]
    list_display = ['centre_type', 'postcode']
    search_fields = ['centre_type', 'postcode']
    form = TestingCentreAdminForm


admin.site.register(Patient, PatientAdmin)
admin.site.register(DiagnosticTest, DiagnosticTestAdmin)
admin.site.register(TestingCentre, CentreAdmin)
