from django.contrib.gis.geos import Point
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from dashboard.models import Patient, TestingCentre, DiagnosticTest
import postcodes_io_api


def get_locations(long, lat):
    api = postcodes_io_api.Api(debug_http=False)
    resp = api.get_nearest_postcodes_for_coordinates(latitude=lat, longitude=long, limit=1)
    result = resp['result'] if ('result' in resp) and (resp['result'] != None) else []
    item = result[0] if len(result) > 0 else {}
    postcode = item['postcode'] if 'postcode' in item else str()
    country = "United Kingdom"
    region = item['region'] if 'region' in item else (item['country'] if 'country' in item else str())

    return {"country": country, "region": region, "postcode": postcode}


class storeJSONSerializer(serializers.Serializer):
    date_test = serializers.DateTimeField()
    test_result = serializers.BooleanField()
    patient_first_name = serializers.CharField(max_length=50)
    patient_last_name = serializers.CharField(max_length=50)
    patient_gender = serializers.CharField(max_length=1)
    patient_dob = serializers.DateField()
    patient_postcode = serializers.CharField(max_length=8)
    testing_centre_type = serializers.CharField(max_length=20)
    testing_centre_long = serializers.FloatField()
    testing_centre_lat = serializers.FloatField()

    def create(self, validated_data):
        print("#######################################")
        print(validated_data['patient_first_name'])
        print("#######################################")

        patient = Patient.objects.create(
            first_name=validated_data['patient_first_name'],
            last_name=validated_data['patient_last_name'],
            gender=validated_data['patient_gender'],
            dob=validated_data['patient_dob'],
            postcode=validated_data['patient_postcode']
        )

        location = get_locations(validated_data['testing_centre_long'], validated_data['testing_centre_lat'])

        testing_centre = TestingCentre.objects.create(
            centre_type=validated_data['testing_centre_type'],
            coordinates=Point(validated_data['testing_centre_long'], validated_data['testing_centre_lat']),
            country=location['country'],
            region=location['region'],
            postcode=location['postcode'],
        )

        diagnostic_test = DiagnosticTest.objects.create(
            testing_centre=testing_centre,
            patient=patient,
            test_result=validated_data['test_result'],
            date_test=validated_data['date_test']
        )

        return diagnostic_test
