# Django Http Response
from django.http import HttpResponse

# Django Rest Framework
from rest_framework import viewsets
from rest_framework import permissions, generics
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from rest_framework.views import APIView

# Django filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

# Serializers
from .api_serializers import TestingCentreSerializer
from .api_serializers import PatientSerializer
from .api_serializers import DiagnosticTestSerializer
from .api_serializers import PostcodeSerializer
from .api_serializers import CustomGeoJSONSerializer

# Models
from .models import Patient, TestingCentre, DiagnosticTest

# Queries to get postcode specific information (i.e. number of tests, positive cases, ...)
from .queries import get_postcode_data


# This viewset and the associated serializer may not be needed. Here now for testing purposes
class PatientViewSet(viewsets.ModelViewSet):
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


# This viewset and the associated serializer may not be needed. Here now for testing purposes
class TestingCentreViewSet(viewsets.ModelViewSet):
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
    class Meta:
        model = DiagnosticTest
        fields = {
            'testing_centre__postcode': ['startswith'],
            'date_test': ['date__lt'],
            'test_result': ['exact'],
            'patient': ['exact'],
        }


# This viewset and the associated serializer may not be needed. Here now for testing purposes
class DiagnosticTestView(generics.ListAPIView):
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


# Used to load data for one specific postcode specified as an argument in the URL
class PostcodeData(generics.ListAPIView):
    queryset = DiagnosticTest.objects.all().order_by('date_test')
    serializer_class = PostcodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request, *args, **kwargs):
        postcode = self.request.query_params.get('postcode', False)
        response = super(PostcodeData, self).list(request, args, kwargs)
        response.data['summary'] = get_postcode_data(postcode)
        return response


# Used to load all testing data with associated coordinates and
# information using a geoJSON format
class GeoView(APIView):
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
                                                 'testing_centre__centre_type',
                                                 'patient__gender',
                                                 'patient'
                                                 )
                                         )

        return HttpResponse(response)
