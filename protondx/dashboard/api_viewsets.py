from rest_framework import viewsets
from rest_framework import permissions, generics
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter

# Django filters
from django_filters.rest_framework import DjangoFilterBackend, FilterSet

from rest_framework import views
from rest_framework.response import Response
from .api_serializers import PatientSerializer, TestingCentreSerializer, DiagnosticTestSerializer, PostcodeSerializer
from .models import Patient, TestingCentre, DiagnosticTest
from .queries import get_postcode_data


# This viewset and the associated serializer may not be needed. Here now for testing purposes
class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('first_name')
    serializer_class = PatientSerializer
    permission_classes = [permissions.IsAuthenticated]

    # -------
    #  Filters
    # -------
    #  Filters
    # search_fields = ('comments', )
    filter_fields = '__all__'
    ordering_fields = '__all__'

    #  Set backends
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter)

    # Enable further filtering
    # filter_class =

    # Define default ordering
    ordering = ('last_name', 'first_name')


# This viewset and the associated serializer may not be needed. Here now for testing purposes
class TestingCentreViewSet(viewsets.ModelViewSet):
    queryset = TestingCentre.objects.all().order_by('centre_type')
    serializer_class = TestingCentreSerializer
    permission_classes = [permissions.IsAuthenticated]

    # -------
    #  Filters
    # -------
    #  Filters
    # search_fields = ('comments', )
    filter_fields = '__all__'
    ordering_fields = '__all__'

    #  Set backends
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter)

    # Enable further filtering
    # filter_class =

    # Define default ordering
    ordering = ('postcode',)


class PostcodeFilter(FilterSet):
    class Meta:
        model = DiagnosticTest
        fields = {
            'testing_centre__postcode': ['startswith'],
            'date_test': ['date__lt'],
            'test_result': ['exact'],
        }


class DiagnosticTestViewSet(generics.ListAPIView):
    queryset = DiagnosticTest.objects.all().order_by('date_test')
    serializer_class = DiagnosticTestSerializer
    # permission_classes = [permissions.IsAuthenticated]

    # -------
    #  Filters
    # -------
    #  Filters
    # search_fields = ('testing_centre__postcode',)
    # filter_fields = ('testing_centre__postcode', 'test_result', 'date_test')
    ordering_fields = '__all__'

    #  Set backends
    filter_backends = (DjangoFilterBackend,
                       SearchFilter,
                       OrderingFilter)

    # Enable further filtering
    filter_class = PostcodeFilter

    # Define default ordering
    ordering = ('date_test',)


class PostcodeData(generics.ListAPIView):
    queryset = DiagnosticTest.objects.all().order_by('date_test')
    serializer_class = PostcodeSerializer

    def list(self, request, *args, **kwargs):
        postcode = self.request.query_params.get('postcode', False)
        response = super(PostcodeData, self).list(request, args, kwargs)
        response.data['summary'] = get_postcode_data(postcode)
        return response


from django.http import HttpResponse
from django.core.serializers import serialize
from rest_framework.views import APIView


class GeoView(APIView):

    def get(self, request):
        result = serialize(
            "geojson",
            TestingCentre.objects.all(),
            srid=4326,
            geometry_field="coordinates",
            fields=(
                "postcode", "centre_type",
            ),
        )

        return HttpResponse(result)
