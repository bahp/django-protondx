#  Django rest framework
from rest_framework import serializers

#  Models
from .models import Patient, DiagnosticTest


# -----------------------------------------------------------------------------
#                             Case Serializer
#  -----------------------------------------------------------------------------
class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'


class DiagnosticTestSerializer(serializers.ModelSerializer):
    # postcode = serializers.CharField(source='testing_centre.postcode')
    # coordinates = serializers.CharField(source='testing_centre.coordinates')
    # centre_type = serializers.CharField(source='testing_centre.centre_type')

    class Meta:
        model = DiagnosticTest
        # fields = ('test_result', 'date_test', 'postcode', 'coordinates', 'centre_type')
        fields = ('test_result', 'date_test', 'postcode', 'coordinates', 'centre_type')


class PostcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticTest
        fields = ''
