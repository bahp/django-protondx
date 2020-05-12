#  Django rest framework
from rest_framework import serializers

#  Models
from .models import Patient, TestingCentre, DiagnosticTest


# -----------------------------------------------------------------------------
#                             Case Serializer
#  -----------------------------------------------------------------------------
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class TestingCentreSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingCentre
        fields = '__all__'


# "type": "Feature", "properties": {"centre_type": "OTHR", "postcode": "IV27 4"}, "geometry": {"type": "Point", "coordinates": [-4.877929687500003, 58.378678539326536]}}

class DiagnosticTestSerializer(serializers.ModelSerializer):
    postcode = serializers.CharField(source='testing_centre.postcode')
    coordinates = serializers.CharField(source='testing_centre.coordinates')
    centre_type = serializers.CharField(source='testing_centre.centre_type')

    class Meta:
        model = DiagnosticTest
        fields = ('test_result', 'date_test', 'postcode', 'coordinates', 'centre_type')


class PostcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticTest
        fields = ''
