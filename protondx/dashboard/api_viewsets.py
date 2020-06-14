"""
This module contains the views and viewsets for the Dashboard App's Django Rest API.
"""

# Django Http Response
from django.http import HttpResponse

# Django Rest Framework
import numpy as np
from rest_framework import viewsets
from rest_framework import permissions, generics
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView
from rest_framework.response import Response

# Django filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

# Serializers
from .api_serializers import TestingCentreSerializer
from .api_serializers import PatientSerializer
from .api_serializers import DiagnosticTestSerializer
from .api_serializers import PostcodeSerializer
from .api_serializers import CustomGeoJSONSerializer
from .api_serializers import DiagnosticDetailSerializer

# Models
from .models import Patient, TestingCentre, DiagnosticTest

# Queries to get postcode specific information (i.e. number of tests, positive cases, ...)
from .queries import get_postcode_data


class PatientViewSet(viewsets.ModelViewSet):
    """
    This class handles the API Patient requests.

    ..todo: Change viewset to ListPI view
    """

    queryset = Patient.objects.all().order_by('first_name')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    # --------------------------
    #  Filter fields and options
    # --------------------------

    #  Filters
    filter_fields = '__all__'
    ordering_fields = '__all__'

    #  Set backends
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter)

    # Define default ordering
    ordering = ('last_name', 'first_name')


class TestingCentreViewSet(viewsets.ModelViewSet):
    """
    This class handles the API TestingCentre requests.

    ..todo: Change viewset to ListPI view
    """

    queryset = TestingCentre.objects.all().order_by('centre_type')
    serializer_class = TestingCentreSerializer
    permission_classes = [permissions.IsAuthenticated]

    # --------------------------
    #  Filter fields and options
    # --------------------------

    #  Filters
    filter_fields = ['centre_type', 'postcode']
    ordering_fields = ['centre_type', 'postcode']

    #  Set backends
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter)

    # Define default ordering
    ordering = ('postcode',)


# Postcode filter rules
class PostcodeFilter(FilterSet):
    """
    This class is the filterset for the 'DiagnosticTestView'.

    It allows queries to filter by postcode, date, result and patient ID.
    """

    class Meta:
        model = DiagnosticTest
        fields = {
            'testing_centre__postcode': ['startswith'],
            'date_test': ['date__lt'],
            'test_result': ['exact'],
            'patient': ['exact'],
        }


class DiagnosticTestView(generics.ListAPIView):
    """
    This view is used to list Diagnostic tests. Queries can filter by postcode, date, result and patient ID.

    Each entry contains the Test ID (PK), the test's date and result and the type of centre it was held at.
    """

    pagination_class = None
    queryset = DiagnosticTest.objects.all().order_by('date_test')
    serializer_class = DiagnosticTestSerializer
    permission_classes = [permissions.IsAuthenticated]

    # --------------------------
    #  Filter fields and options
    # --------------------------

    #  Filters
    ordering_fields = '__all__'

    #  Set backends
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter)

    # Enable further filtering
    filter_class = PostcodeFilter

    # Define default ordering
    ordering = ('date_test',)


class DiagnosticDetailView(generics.ListAPIView):
    """
    This view is used to obtain detailed information relating to a diagnostic test.
    The comment relating to a diagnostic is returned.

    The test ID must be provided and users must be authenticated.

    e.g. /?id=127885
    """
    queryset = DiagnosticTest.objects.only('comment', 'test_result', 'id')
    serializer_class = DiagnosticDetailSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_fields = ['id']

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data

        labels = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2,
                  2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4, 4.1,
                  4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6, 6.1, 6.2,
                  6.3, 6.4, 6.5, 6.6, 6.7, 6.8, 6.9, 7, 7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7, 7.8, 7.9, 8, 8.1, 8.2, 8.3,
                  8.4, 8.5, 8.6, 8.7, 8.8, 8.9, 9, 9.1, 9.2, 9.3, 9.4, 9.5, 9.6, 9.7, 9.8, 9.9, 10, 10.1, 10.2, 10.3,
                  10.4, 10.5, 10.6, 10.7, 10.8, 10.9, 11, 11.1, 11.2, 11.3, 11.4, 11.5, 11.6, 11.7, 11.8, 11.9, 12,
                  12.1, 12.2, 12.3, 12.4, 12.5, 12.6, 12.7, 12.8, 12.9, 13, 13.1, 13.2, 13.3, 13.4, 13.5, 13.6, 13.7,
                  13.8, 13.9, 14, 14.1, 14.2, 14.3, 14.4, 14.5, 14.6, 14.7, 14.8, 14.9, 15, 15.1, 15.2, 15.3, 15.4,
                  15.5, 15.6, 15.7, 15.8, 15.9, 16, 16.1, 16.2, 16.3, 16.4, 16.5, 16.6, 16.7, 16.8, 16.9, 17, 17.1,
                  17.2, 17.3, 17.4, 17.5, 17.6, 17.7, 17.8, 17.9, 18, 18.1, 18.2, 18.3, 18.4, 18.5, 18.6, 18.7, 18.8,
                  18.9, 19, 19.1, 19.2, 19.3, 19.4, 19.5, 19.6, 19.7, 19.8, 19.9]

        y = []

        StartAmpTime = 3.3
        EndAmpTime = StartAmpTime + 10.0
        if not response_list[0]['test_result']:
            y = [round(0.05 + np.random.uniform(0, 0.02), 3) for _ in labels]
        else:
            for t in labels:
                Pos = 0.05 + np.random.uniform(0, 0.02)
                if StartAmpTime <= t <= EndAmpTime:
                    x = 2 * (t - StartAmpTime) - 10
                    Pos += (1 / (1 + np.exp(-x))) * 0.9
                elif t > EndAmpTime:
                    x = 2 * (EndAmpTime - StartAmpTime) - 10
                    Pos += (1 / (1 + np.exp(-x))) * 0.9

                y.append(round(Pos, 3))

        pcr_data = {
            "x": [str(i) for i in labels],
            "y": y
        }

        response_list.append(pcr_data)

        return Response(response_list)

    def get_paginated_response(self, data):
        return Response(data)


class PostcodeData(generics.ListAPIView):
    """
    This view is used to obtain Diagnostic statistics related to one postcode.
    It provides the total number of experiments,
    the number of positive and negative diagnostics and the number of patients tested.

    The postcode must be specified as a query argument.
    e.g. /?postcode=SW5 0TU
    """

    queryset = DiagnosticTest.objects.all().order_by('date_test')
    serializer_class = PostcodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        postcode = self.request.query_params.get('postcode', False)
        response = super(PostcodeData, self).list(request, args, kwargs)
        response.data['summary'] = get_postcode_data(postcode)
        return response


class GeoView(APIView):
    """
    This view is used to obtain Diagnostic Test data from the database. It provides all tests and their associated
    coordinates and information in a GeoJSON format.
    Each returned feature will have the form:

    {"type": "Feature",
     "properties": {
        "date_test": string,
        "patient": int,
        "test_result": string,
        "testing_centre__postcode": string,
        "testing_centre__county": string,
        "testing_centre__region": string,
        "testing_centre__country": string,
        "testing_centre__centre_type": string,
        "patient__gender": string,
        "pk": string},
     "geometry": {"type": "Point", "coordinates": [float, float]}}

    """

    permission_classes = []

    def get(self, request):
        serializers = CustomGeoJSONSerializer()
        data = DiagnosticTest.objects.all()
        response = serializers.serialize(data,
                                         geometry_field='testing_centre__coordinates',
                                         fields=('pk',
                                                 'date_test',
                                                 'test_result',
                                                 'testing_centre__postcode',
                                                 'testing_centre__county',
                                                 'testing_centre__region',
                                                 'testing_centre__country',
                                                 'testing_centre__centre_type',
                                                 'patient__gender',
                                                 'patient'
                                                 )
                                         )

        return HttpResponse(response)
