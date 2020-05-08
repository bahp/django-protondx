from rest_framework import viewsets
from rest_framework import views
from rest_framework.response import Response
from .api_serializers import PatientSerializer, TestingCentreSerializer, DiagnosticTestSerializer #, PopupSerializer
from .models import Patient, TestingCentre, DiagnosticTest


class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all().order_by('first_name')
    serializer_class = PatientSerializer


class TestingCentreViewSet(viewsets.ModelViewSet):
    queryset = TestingCentre.objects.all().order_by('centre_type')
    serializer_class = TestingCentreSerializer


class DiagnosticTestViewSet(viewsets.ModelViewSet):
    queryset = DiagnosticTest.objects.all().order_by('date_test')
    serializer_class = DiagnosticTestSerializer

    def get_queryset(self):
        postcode = self.request.query_params.get('postcode', False)
        if postcode:
            tests = DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode)
        else:
            tests = DiagnosticTest.objects.all().order_by('date_test')
        return tests


# def get_postcode_total_experiments(postcode):
#     return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode).count()
#
#
# def get_postcode_negative_experiments(postcode):
#     return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode, test_result=False).count()
#
#
# def get_postcode_positive_experiments(postcode):
#     return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode, test_result=True).count()
#
#
# def get_postcode_individuals_tested(postcode):
#     return DiagnosticTest \
#         .objects \
#         .select_related('patient', 'testing_centre') \
#         .filter(testing_centre__postcode__startswith=postcode) \
#         .values('patient_id') \
#         .distinct() \
#         .count()
#
#
# def get_postcode_data(postcode):
#     data = {
#         'total': get_postcode_total_experiments(postcode),
#         'positive': get_postcode_positive_experiments(postcode),
#         'negative': get_postcode_negative_experiments(postcode),
#         'patients': get_postcode_individuals_tested(postcode),
#     }
#
#     return data
#
#
# class PopupViewSet(views.APIView):
#     @classmethod
#     def get_extra_actions(cls):
#         return []
#
#     def get(self, request, *args, **kw):
#         postcode = request.GET.get('postcode', None)
#         data = get_postcode_data(postcode)
#         results = PopupSerializer(data, many=True).data
#         return Response(results)
