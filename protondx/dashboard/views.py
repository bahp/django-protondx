from django.shortcuts import render
from django.views.generic import TemplateView

from .models import Patient, TestingCentre, DiagnosticTest
from .forms import PostcodeForm


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

class DashView(TemplateView):
    template_name = 'dashboard/dash.html'

    # #####
    # remove test entries from context
    # #####
    def get(self, request, **kwargs):
        form = PostcodeForm()
        context = {
            'count_total_exp': get_total_experiments(),
            'count_pos_exp': get_positive_experiments(),
            'count_neg_exp': get_negative_experiments(),
            'count_indiv_patients': get_individuals_tested(),
            'test1': get_postcode_data('SW5 0TU'),
            'test2': get_postcode_data('SW1A 1AA'),
            'form': form,
        }
        return render(request, self.template_name, context)

    # Not currently used (Might be useful when querying postcode info)
    def post(self, request):
        form = PostcodeForm(request.POST)
        if form.is_valid():
            post_code_query = get_postcode_data(form.cleaned_data['post'])
            form = PostcodeForm()
            context = {
                'count_total_exp': get_total_experiments(),
                'count_pos_exp': get_positive_experiments(),
                'count_neg_exp': get_negative_experiments(),
                'count_indiv_patients': get_individuals_tested(),
                'test1': get_postcode_data('SW5 0TU'),
                'test2': get_postcode_data('SW1A 1AA'),
                'form': form,
                'post_code_query': post_code_query
            }
            return render(request, self.template_name, context)
