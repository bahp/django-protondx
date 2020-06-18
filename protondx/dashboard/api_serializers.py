"""
This module contains the serializers for the Dashboard App's Django Rest API.
"""

#  Serializer imports
from datetime import datetime

from rest_framework import serializers
from django.contrib.gis.serializers.geojson import Serializer as GeoJSONSerializer
from django.utils.encoding import is_protected_type

#  Models
from .models import Patient, DiagnosticTest, TestingCentre


class PatientSerializer(serializers.ModelSerializer):
    """
    Used to serialize Patient information to JSON.
    """

    gender = serializers.CharField(source='get_gender_display')
    dob = serializers.DateField(format="%d-%m-%Y", required=False, read_only=True)

    class Meta:
        model = Patient
        fields = ['gender', 'dob', 'postcode', 'first_name', 'last_name']


class DiagnosticTestSerializer(serializers.ModelSerializer):
    """
    Used to serialize general DiagnosticTest information (date, result, centre_type) to JSON.
    """

    test_result = serializers.CharField(source='get_test_result_display')
    centre_type = serializers.CharField(source='testing_centre.centre_type')
    date_test = serializers.DateTimeField(format="%d-%m-%Y", required=False, read_only=True)

    class Meta:
        model = DiagnosticTest
        fields = ['test_result', 'centre_type', 'date_test', 'id']


class DiagnosticDetailSerializer(serializers.ModelSerializer):
    """
    Used to serialize detailed Diagnostic test information (e.g. clinician comment) to JSON.
    """

    class Meta:
        model = DiagnosticTest
        fields = ['comment', 'id', 'test_result']


class TestingCentreSerializer(serializers.ModelSerializer):
    """
    Used to serialize TestingCentre information to JSON.
    """

    class Meta:
        model = TestingCentre
        fields = ['centre_type', 'postcode']


class PostcodeSerializer(serializers.ModelSerializer):
    """
    Used to serialize postcode level information summaries to JSON. No detailed information is serialized.
    """

    class Meta:
        model = DiagnosticTest
        fields = ''


class CustomGeoJSONSerializer(GeoJSONSerializer):
    """
    Converts a queryset which has columns linked to by a foreign key to GeoJSON.
    """

    def end_object(self, obj):
        for field in self.selected_fields:
            if field == 'pk':
                continue
            elif field in self._current.keys():
                continue
            else:
                try:
                    if '__' in field:
                        fields = field.split('__')
                        value = obj
                        for f in fields:
                            value = getattr(value, f)
                        if self.geometry_field == field:
                            self._geometry = value
                        elif value != obj:
                            self._current[field] = value

                except AttributeError:
                    pass

        super(CustomGeoJSONSerializer, self).end_object(obj)

    def _value_from_field(self, obj, field):
        value = field.value_from_object(obj)

        # Use display name for test result
        if str(field) == "dashboard.DiagnosticTest.test_result":
            return obj.get_test_result_display()
        # Format test date to human readable format (discard time)
        elif str(field) == "dashboard.DiagnosticTest.date_test":
            return int(obj.date_test.timestamp())
        elif is_protected_type(value):
            return value
        else:
            return field.value_to_string(obj)
