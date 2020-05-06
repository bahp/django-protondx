from django.shortcuts import render
from django.views import generic

from .models import Patient, TestingCentre, DiagnosticTest


# --------------
# QUERIES
# --------------

def get_total_experiments():
    return DiagnosticTest.objects.count()


def get_negative_experiments():
    return DiagnosticTest.objects.filter(test_result=False).count()


def get_positive_experiments():
    return DiagnosticTest.objects.filter(test_result=True).count()


def get_individuals_tested():
    return Patient.objects.count()


def get_postcode_total_experiments(postcode):
    return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode).count()


def get_postcode_negative_experiments(postcode):
    return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode, test_result=False).count()


def get_postcode_positive_experiments(postcode):
    return DiagnosticTest.objects.filter(testing_centre__postcode__startswith=postcode, test_result=True).count()


def get_postcode_individuals_tested(postcode):
    return DiagnosticTest \
        .objects \
        .select_related('patient', 'testing_centre') \
        .filter(testing_centre__postcode__startswith=postcode) \
        .values('patient_id') \
        .distinct() \
        .count()


def get_postcode_data(postcode):
    data = {
        'total': get_postcode_total_experiments(postcode),
        'positive': get_postcode_positive_experiments(postcode),
        'negative': get_postcode_negative_experiments(postcode),
        'patients': get_postcode_individuals_tested(postcode),
    }

    return data


# --------------
# VIEWS
# --------------

def DashView(request):
    context = {
        'count_total_exp': get_total_experiments(),
        'count_pos_exp': get_positive_experiments(),
        'count_neg_exp': get_negative_experiments(),
        'count_indiv_patients': get_individuals_tested(),
        'test1': get_postcode_data('SW5 0TU'),
        'test2': get_postcode_data('SW1A 1AA'),
    }

    return render(request, 'dashboard/dash.html', context)


def request_page(request):
    if request.GET.get('mybtn'):
        context = {'result': get_postcode_data(request.GET.get('post_code'))}
        return render(request, 'dashboard/dash.html', context)
