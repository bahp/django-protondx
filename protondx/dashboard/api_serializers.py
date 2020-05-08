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


class DiagnosticTestSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticTest
        fields = '__all__'


# class PopupSerializer(serializers.Serializer):
#     total = serializers.IntegerField()
#     positive = serializers.IntegerField()
#     negative = serializers.IntegerField()
#     patients = serializers.IntegerField()
