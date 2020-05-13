#  Serializer imports
from rest_framework import serializers
from django.contrib.gis.serializers.geojson import Serializer as GeoJSONSerializer

#  Models
from .models import Patient, DiagnosticTest, TestingCentre


# Serializer for patient information (Not currently used)
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


# Serializer for Diagnostic tests (Not currently used)
class DiagnosticTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticTest
        fields = '__all__'


# Serializer for Testing Centres (Not currently used)
class TestingCentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingCentre
        fields = '__all__'


# Serializer for Postcode Popup
class PostcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticTest
        fields = ''


# Serializer for all testing data and associated coordinates
class CustomGeoJSONSerializer(GeoJSONSerializer):

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
